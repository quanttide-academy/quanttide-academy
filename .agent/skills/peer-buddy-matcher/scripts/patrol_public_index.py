#!/usr/bin/env python3
"""Host-agnostic Public Index patrol script supporting Layer 0 (full) and Layer 1 (incremental).

Reads the QuantTide Public Index Feishu Cloud Doc (`W90qdp8azogcCZxCNGfcEEWonuc` by default)
via local `lark-cli`, separates `self` from `peers`, parses structured `[B-YYYYMMDD-NN｜STATUS]`
blockers, and tracks per-peer content hashes in `career-discovery/.patrol-state.json`.

In Layer 1 mode (`--since-last-patrol`):
  - Ignores edits to your own card so publishing via `cit-reflection` never triggers false noise.
  - Returns `status: "no_changes"` when no peer added or changed their card/blockers.
  - Returns `status: "has_updates"` with only `changed_peers` when real peer updates exist.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

DEFAULT_REGISTRY_DOC = "W90qdp8azogcCZxCNGfcEEWonuc"
BLOCKER_RE = re.compile(
    r"\[(B-\d{8}-\d{2})\s*[｜|]\s*(OPEN|RESPONDED|RESOLVED|ESCALATED)\]\s*([^\[;\n]+)"
)


def find_lark_cli() -> str | None:
    for candidate in (
        Path.home() / ".local" / "bin" / "lark-cli",
        Path.home() / ".homebrew" / "bin" / "lark-cli",
        Path("/opt/homebrew/bin/lark-cli"),
        Path("/usr/local/bin/lark-cli"),
    ):
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return shutil.which("lark-cli")


def run_cmd(cmd: list[str], timeout: int = 30) -> subprocess.CompletedProcess[str]:
    env = dict(os.environ)
    env.setdefault("LARK_CLI_NO_PROXY_WARN", "1")
    return subprocess.run(
        cmd,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=timeout,
        env=env,
        check=False,
    )


def extract_doc_token(doc_ref: str) -> str:
    raw = (doc_ref or "").strip()
    if not raw:
        return ""
    m = re.search(r"/(?:docx|docs|wiki)/([A-Za-z0-9_-]+)", raw)
    return m.group(1) if m else raw


def get_feishu_identity(lark_bin: str) -> tuple[str, str]:
    proc = run_cmd([lark_bin, "whoami"], timeout=15)
    if proc.returncode == 0:
        try:
            payload = json.loads(proc.stdout)
            behalf = payload.get("onBehalfOf") or {}
            return str(behalf.get("openId") or "").strip(), str(behalf.get("userName") or "").strip()
        except json.JSONDecodeError:
            pass
    return "", ""


def _elem_text_with_breaks(elem: ET.Element) -> str:
    parts: list[str] = []

    def walk(node: ET.Element) -> None:
        if node.tag == "br":
            parts.append("\n")
            return
        if node.tag == "cite" and node.attrib.get("type") == "user":
            uname = node.attrib.get("user-name") or node.attrib.get("user-id") or ""
            if uname:
                parts.append(uname)
            return
        if node.text:
            parts.append(node.text)
        for child in node:
            walk(child)
            if child.tail:
                parts.append(child.tail)

    walk(elem)
    return "".join(parts)


def parse_blockers(raw_blockers: str, sla_hours: int) -> list[dict[str, Any]]:
    text = (raw_blockers or "").strip()
    if not text or "暂无" in text:
        return []

    now = dt.datetime.now()
    items: list[dict[str, Any]] = []
    for match in BLOCKER_RE.finditer(text):
        bid, status, desc = match.group(1), match.group(2), match.group(3).strip(" ；;。")
        age_hours: float | None = None
        overdue = False
        try:
            b_date = dt.datetime.strptime(bid[2:10], "%Y%m%d")
            age_hours = round(max(0.0, (now - b_date).total_seconds() / 3600.0), 1)
            overdue = status == "OPEN" and age_hours >= sla_hours
        except ValueError:
            pass
        items.append(
            {
                "blocker_id": bid,
                "status": status,
                "summary": desc,
                "age_hours_approx": age_hours,
                "overdue_sla": overdue,
            }
        )

    if not items and text:
        items.append(
            {
                "blocker_id": "UNSTRUCTURED",
                "status": "OPEN",
                "summary": text[:200],
                "age_hours_approx": None,
                "overdue_sla": False,
            }
        )
    return items


def peer_fingerprint(card: dict[str, Any]) -> str:
    stable = "|".join(
        [
            str(card.get("updated_at") or ""),
            str(card.get("offer") or ""),
            str(card.get("seek") or ""),
            str(card.get("avoid") or ""),
            str(card.get("experiment") or ""),
            str(card.get("playbooks") or ""),
            str(card.get("active_blockers_raw") or ""),
        ]
    )
    return hashlib.sha256(stable.encode("utf-8")).hexdigest()[:16]


def parse_member_cards(xml_content: str, sla_hours: int) -> list[dict[str, Any]]:
    members: list[dict[str, Any]] = []
    try:
        root = ET.fromstring(f"<doc>{xml_content}</doc>")
    except ET.ParseError:
        return members

    for elem in root:
        if elem.tag != "callout":
            continue
        raw_text = "\n".join(_elem_text_with_breaks(p) for p in elem.findall("p"))
        if "Offer（我能兜底）" not in raw_text and "id:ou_" not in raw_text and "一句话搭伙切口" not in raw_text:
            continue

        open_id = ""
        user_name = ""
        homepage_url = ""
        for cite in elem.iter("cite"):
            if cite.attrib.get("type") == "user" and not open_id:
                open_id = cite.attrib.get("user-id", "")
                user_name = cite.attrib.get("user-name", "")
        for link in elem.iter("a"):
            if link.attrib.get("href") and not homepage_url:
                homepage_url = link.attrib["href"]
        if not open_id:
            m_id = re.search(r"\bid:(ou_[A-Za-z0-9_-]+)", raw_text)
            if m_id:
                open_id = m_id.group(1)

        def grab(pattern: str) -> str:
            m = re.search(pattern, raw_text)
            return m.group(1).strip() if m else ""

        raw_blockers = grab(r"Active-Blockers）[：:]\s*([^\n]+)")
        card = {
            "block_id": elem.attrib.get("id", ""),
            "open_id": open_id,
            "user_name": user_name,
            "homepage_url": homepage_url,
            "updated_at": grab(r"更新[：:]\s*([0-9]{4}-[0-9]{2}-[0-9]{2})"),
            "intro": grab(r"一句话搭伙切口[：:]\s*([^\n]+)"),
            "offer": grab(r"Offer（我能兜底）[：:]\s*([^\n]+)"),
            "seek": grab(r"Seek（想找同路人）[：:]\s*([^\n]+)"),
            "avoid": grab(r"Avoid（协作边界）[：:]\s*([^\n]+)"),
            "rhythm": grab(r"投入节奏与时段[：:]\s*([^\n]+)"),
            "experiment": grab(r"2 周微实验[：:]\s*([^\n]+)"),
            "playbooks": grab(r"Playbooks）[：:]\s*([^\n]+)"),
            "active_blockers_raw": raw_blockers,
            "parsed_blockers": parse_blockers(raw_blockers, sla_hours),
        }
        card["content_hash"] = peer_fingerprint(card)
        members.append(card)
    return members


def resolve_registry_doc(cli_doc: str, state_path: Path | None) -> str:
    if cli_doc:
        return extract_doc_token(cli_doc)
    if state_path and state_path.is_file():
        try:
            st = json.loads(state_path.read_text(encoding="utf-8"))
            if isinstance(st, dict) and st.get("registry_doc_id"):
                return extract_doc_token(str(st["registry_doc_id"]))
        except json.JSONDecodeError:
            pass
    return extract_doc_token(os.environ.get("QT_PUBLIC_INDEX_DOC", "")) or DEFAULT_REGISTRY_DOC


def load_patrol_state(path: Path) -> dict[str, Any]:
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except json.JSONDecodeError:
            pass
    return {"last_revision_id": None, "last_checked_at": None, "peer_hashes": {}}


def save_patrol_state(path: Path, state: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry-doc", default="", help="Public Index Feishu doc token or URL.")
    parser.add_argument("--state", type=Path, default=Path("career-discovery/.card-link.json"))
    parser.add_argument(
        "--patrol-state",
        type=Path,
        default=Path("career-discovery/.patrol-state.json"),
        help="Local cursor storing last seen peer hashes for Layer 1 incremental checks.",
    )
    parser.add_argument(
        "--since-last-patrol",
        action="store_true",
        help="Layer 1 incremental mode: return status=no_changes if no peer card changed since last patrol.",
    )
    parser.add_argument(
        "--mark-seen",
        action="store_true",
        help="Persist current peer hashes to --patrol-state after scanning.",
    )
    parser.add_argument("--sla-hours", type=int, default=48, help="Hours before an OPEN blocker is flagged SLA-overdue.")
    args = parser.parse_args()

    lark_bin = find_lark_cli()
    if not lark_bin:
        print(json.dumps({"status": "unavailable", "reason": "lark_cli_not_found"}, ensure_ascii=False))
        return 0

    doc_id = resolve_registry_doc(args.registry_doc, args.state)
    proc = run_cmd(
        [
            lark_bin,
            "docs",
            "+fetch",
            "--as",
            "user",
            "--doc",
            doc_id,
            "--detail",
            "with-ids",
            "--doc-format",
            "xml",
            "--scope",
            "full",
        ]
    )
    if proc.returncode != 0:
        print(
            json.dumps(
                {"status": "error", "error": (proc.stderr or proc.stdout).strip()[:300]},
                ensure_ascii=False,
                indent=2,
            )
        )
        return 1

    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        print(json.dumps({"status": "error", "error": "invalid_json_from_fetch"}, ensure_ascii=False))
        return 1

    doc_obj = (payload.get("data") or {}).get("document") or {}
    content = doc_obj.get("content") or ""
    revision_id = doc_obj.get("revision_id")

    my_open_id, my_name = get_feishu_identity(lark_bin)
    all_members = parse_member_cards(content, args.sla_hours)

    self_card: dict[str, Any] | None = None
    peers: list[dict[str, Any]] = []
    for m in all_members:
        if my_open_id and m.get("open_id") == my_open_id:
            self_card = m
        else:
            peers.append(m)

    prev_state = load_patrol_state(args.patrol_state)
    prev_hashes: dict[str, str] = prev_state.get("peer_hashes") or {}
    current_hashes: dict[str, str] = {}
    changed_peers: list[dict[str, Any]] = []

    for p in peers:
        pkey = p.get("open_id") or p.get("block_id") or p.get("user_name") or ""
        chash = p["content_hash"]
        current_hashes[pkey] = chash
        if prev_hashes.get(pkey) != chash:
            changed_peers.append(p)

    if args.mark_seen:
        save_patrol_state(
            args.patrol_state,
            {
                "registry_doc_id": doc_id,
                "last_revision_id": revision_id,
                "last_checked_at": dt.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "peer_hashes": current_hashes,
            },
        )

    overdue_self_blockers = [
        b for b in (self_card["parsed_blockers"] if self_card else []) if b["overdue_sla"]
    ]

    if args.since_last_patrol and not changed_peers:
        print(
            json.dumps(
                {
                    "status": "no_changes",
                    "mode": "layer1_incremental",
                    "registry_doc_id": doc_id,
                    "revision_id": revision_id,
                    "peer_count": len(peers),
                    "changed_peer_count": 0,
                    "overdue_self_blockers": overdue_self_blockers,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return 0

    target_peers = changed_peers if args.since_last_patrol else peers
    open_peer_blockers = [
        {
            "peer_name": p["user_name"],
            "peer_open_id": p["open_id"],
            "homepage_url": p["homepage_url"],
            **b,
        }
        for p in target_peers
        for b in p["parsed_blockers"]
        if b["status"] == "OPEN"
    ]

    print(
        json.dumps(
            {
                "status": "has_updates" if args.since_last_patrol else "ok",
                "mode": "layer1_incremental" if args.since_last_patrol else "layer0_full",
                "registry_doc_id": doc_id,
                "revision_id": revision_id,
                "sla_hours": args.sla_hours,
                "self_identity": {"open_id": my_open_id, "user_name": my_name},
                "total_members_in_index": len(all_members),
                "peer_count": len(peers),
                "changed_peer_count": len(changed_peers),
                "self_card": self_card,
                "overdue_self_blockers": overdue_self_blockers,
                "open_peer_blockers": open_peer_blockers,
                "peers": target_peers,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
