#!/usr/bin/env python3
"""Local CIT reflection journal, requester-confirmed blocker ledger, and optional Public Index sync.

Maintains two private local files under `cit-reflection/`:
  - `cit-reflection/journal.md`:  Append-only private CIT reflections & decision context (NEVER uploaded).
  - `cit-reflection/ledger.json`: Structured `困惑 → 回应` ledger supporting OPEN/RESOLVED tracking
                                  and zero-form informal DM/voice help archival.

ONLY when `--confirm-publish` is explicitly passed after member review does this script update the
`## 动态脉冲` section of `career-discovery/partner-card.md` and sync the student's single `<callout>`
block in the QuantTide Public Index Feishu Cloud Doc (`W90qdp8azogcCZxCNGfcEEWonuc`).
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

DEFAULT_REGISTRY_DOC = "W90qdp8azogcCZxCNGfcEEWonuc"


def load_ledger(path: Path) -> dict[str, Any]:
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                data.setdefault("blockers", [])
                data.setdefault("playbooks_latest", "")
                return data
        except json.JSONDecodeError:
            pass
    return {"schema_version": "qt-coordination-ledger/v1", "playbooks_latest": "", "blockers": []}


def save_ledger(path: Path, ledger: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def append_journal(path: Path, entry_md: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.is_file():
        path.write_text(
            "# 个人关键事件反思与困惑闭环日志（私享｜仅留本地）\n\n",
            encoding="utf-8",
        )
    with path.open("a", encoding="utf-8") as fh:
        fh.write(entry_md.rstrip() + "\n\n")


def next_blocker_id(ledger: dict[str, Any], today_str: str) -> str:
    prefix = f"B-{today_str.replace('-', '')}-"
    existing_nums = []
    for b in ledger.get("blockers") or []:
        bid = str(b.get("blocker_id") or "")
        if bid.startswith(prefix):
            tail = bid[len(prefix) :]
            if tail.isdigit():
                existing_nums.append(int(tail))
    seq = max(existing_nums, default=0) + 1
    return f"{prefix}{seq:02d}"


def format_open_blockers_line(ledger: dict[str, Any]) -> str:
    open_items = [
        f"[{b['blocker_id']}｜OPEN] {b['summary']}"
        for b in (ledger.get("blockers") or [])
        if b.get("status") == "OPEN"
    ]
    return "；".join(open_items) if open_items else "暂无挂出困惑"


def update_partner_card_pulse(card_path: Path, playbooks: str, blockers_line: str) -> bool:
    if not card_path.is_file():
        return False
    text = card_path.read_text(encoding="utf-8")
    pb_val = playbooks.strip() or "暂无（待日常反思补充）"
    ab_val = blockers_line.strip() or "暂无挂出困惑"
    pulse_block = (
        "## 动态脉冲（可选｜供同伴 AI 巡检与搭伙撮合）\n"
        f"- **Progress & Playbooks（近期进展与可复用经验）**：{pb_val}\n"
        f"- **Active-Blockers（当前活跃困惑）**：{ab_val}\n"
    )

    pattern = re.compile(
        r"##\s*动态脉冲[^\n]*\n.*?(?=\n---\s*\nGenerated-At:|\Z)",
        re.DOTALL,
    )
    if pattern.search(text):
        new_text = pattern.sub(pulse_block.rstrip(), text, count=1)
    elif "Generated-At:" in text:
        new_text = re.sub(
            r"\n---\s*\nGenerated-At:",
            f"\n---\n\n{pulse_block}\n---\nGenerated-At:",
            text,
            count=1,
        )
    else:
        new_text = text.rstrip() + "\n\n---\n\n" + pulse_block

    today = dt.date.today().isoformat()
    new_text = re.sub(r"Generated-At:\s*[0-9-]+", f"Generated-At: {today}", new_text)
    new_text = re.sub(r"Schema-Version:\s*qt-partner-card/v1\b", "Schema-Version: qt-partner-card/v1.1", new_text)
    card_path.write_text(new_text, encoding="utf-8")
    return True


def find_sync_public_index_script() -> Path | None:
    here = Path(__file__).resolve()
    candidates = [
        here.parents[2] / "career-discovery-interview" / "scripts" / "sync_public_index.py",
        Path(".agents/skills/career-discovery-interview/scripts/sync_public_index.py"),
        Path(".agent/skills/career-discovery-interview/scripts/sync_public_index.py"),
    ]
    for c in candidates:
        if c.is_file():
            return c
    return None


def sync_to_public_index(
    registry_doc: str, card_path: Path, state_path: Path
) -> dict[str, Any]:
    script = find_sync_public_index_script()
    if not script:
        return {"status": "skipped", "reason": "sync_public_index_script_not_found"}
    env = dict(os.environ)
    env.setdefault("LARK_CLI_NO_PROXY_WARN", "1")
    proc = subprocess.run(
        [
            sys.executable,
            str(script),
            "--mode",
            "upsert",
            "--registry-doc",
            registry_doc,
            "--card",
            str(card_path),
            "--state",
            str(state_path),
            "--confirm-registry",
        ],
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=60,
        env=env,
        check=False,
    )
    if proc.returncode != 0:
        return {"status": "error", "error": (proc.stderr or proc.stdout).strip()[:300]}
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"status": "ok", "raw": proc.stdout.strip()[:200]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("reflect", "resolve", "informal-resolve"),
        required=True,
    )
    parser.add_argument("--trigger", choices=("daily", "milestone", "stuck", "pivot"), default="daily")
    parser.add_argument("--playbooks", default="", help="Progress & reusable playbooks summary.")
    parser.add_argument("--context", default="", help="Private decision context / sense-making (local journal only).")
    parser.add_argument("--blocker", default="", help="Concrete blocker description (for reflect or informal-resolve).")
    parser.add_argument("--blocker-id", default="", help="Existing blocker ID to resolve (for --mode resolve).")
    parser.add_argument("--helper", default="", help="Peer or escalation owner who helped resolve the blocker.")
    parser.add_argument("--resolution", default="", help="1-line summary of how the blocker was solved.")
    parser.add_argument(
        "--channel",
        choices=("public_index", "feishu_dm", "voice", "group_reply", "escalation"),
        default="feishu_dm",
    )
    parser.add_argument("--data-dir", type=Path, default=Path("cit-reflection"))
    parser.add_argument("--card", type=Path, default=Path("career-discovery/partner-card.md"))
    parser.add_argument("--state", type=Path, default=Path("career-discovery/.card-link.json"))
    parser.add_argument("--registry-doc", default=DEFAULT_REGISTRY_DOC)
    parser.add_argument(
        "--confirm-publish",
        action="store_true",
        help="Explicit member consent gate to update partner-card.md and sync the Public Index Cloud Doc.",
    )
    args = parser.parse_args()

    today = dt.date.today().isoformat()
    now_iso = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    journal_path = args.data_dir / "journal.md"
    ledger_path = args.data_dir / "ledger.json"
    ledger = load_ledger(ledger_path)

    result: dict[str, Any] = {"status": "ok", "mode": args.mode, "timestamp": now_iso}

    if args.mode == "reflect":
        if args.playbooks.strip():
            ledger["playbooks_latest"] = args.playbooks.strip()
        new_bid = ""
        if args.blocker.strip():
            new_bid = next_blocker_id(ledger, today)
            ledger["blockers"].append(
                {
                    "blocker_id": new_bid,
                    "status": "OPEN",
                    "trigger": args.trigger,
                    "summary": args.blocker.strip(),
                    "created_at": now_iso,
                    "resolved_at": None,
                    "helper": None,
                    "resolution": None,
                    "channel": None,
                    "requester_confirmed": False,
                }
            )
            result["created_blocker_id"] = new_bid

        save_ledger(ledger_path, ledger)
        journal_lines = [f"## {now_iso}｜CIT 反思（触发：{args.trigger}）"]
        if args.playbooks.strip():
            journal_lines.append(f"- **进展与可复用经验**：{args.playbooks.strip()}")
        if args.context.strip():
            journal_lines.append(f"- **决策上下文与意义感（私享）**：{args.context.strip()}")
        if new_bid:
            journal_lines.append(f"- **新增活跃困惑**：`[{new_bid}｜OPEN]` {args.blocker.strip()}")
        append_journal(journal_path, "\n".join(journal_lines))

    elif args.mode == "resolve":
        if not args.blocker_id.strip():
            print(json.dumps({"status": "error", "error": "missing_blocker_id"}, ensure_ascii=False))
            return 1
        found = None
        for b in ledger["blockers"]:
            if b.get("blocker_id") == args.blocker_id.strip():
                found = b
                break
        if not found:
            print(json.dumps({"status": "error", "error": f"blocker_not_found:{args.blocker_id}"}, ensure_ascii=False))
            return 1
        found["status"] = "RESOLVED"
        found["resolved_at"] = now_iso
        found["helper"] = args.helper.strip() or "同伴"
        found["resolution"] = args.resolution.strip() or "已由提问者确认解决"
        found["channel"] = args.channel
        found["requester_confirmed"] = True
        save_ledger(ledger_path, ledger)
        append_journal(
            journal_path,
            f"## {now_iso}｜困惑闭环确认（`{found['blocker_id']}`）\n"
            f"- **原困惑**：{found['summary']}\n"
            f"- **解答同伴**：{found['helper']}（渠道：`{found['channel']}`）\n"
            f"- **解决方式（提问者本人确认有效）**：{found['resolution']}",
        )
        result["resolved_blocker_id"] = found["blocker_id"]

    elif args.mode == "informal-resolve":
        if not args.blocker.strip():
            print(json.dumps({"status": "error", "error": "missing_blocker_description"}, ensure_ascii=False))
            return 1
        bid = next_blocker_id(ledger, today)
        ledger["blockers"].append(
            {
                "blocker_id": bid,
                "status": "RESOLVED",
                "trigger": "informal_help",
                "summary": args.blocker.strip(),
                "created_at": now_iso,
                "resolved_at": now_iso,
                "helper": args.helper.strip() or "同伴",
                "resolution": args.resolution.strip() or "私聊/语音顺手协助解决",
                "channel": args.channel,
                "requester_confirmed": True,
            }
        )
        save_ledger(ledger_path, ledger)
        append_journal(
            journal_path,
            f"## {now_iso}｜非正式互助顺手归档（`{bid}`）\n"
            f"- **解决的问题**：{args.blocker.strip()}\n"
            f"- **帮忙同伴**：{args.helper.strip() or '同伴'}（渠道：`{args.channel}`）\n"
            f"- **解决方式（提问者本人确认）**：{args.resolution.strip() or '私聊/语音顺手协助解决'}",
        )
        result["archived_blocker_id"] = bid

    open_line = format_open_blockers_line(ledger)
    result["open_blockers_count"] = sum(1 for b in ledger["blockers"] if b.get("status") == "OPEN")
    result["resolved_blockers_count"] = sum(1 for b in ledger["blockers"] if b.get("status") == "RESOLVED")
    result["public_preview"] = {
        "playbooks": ledger.get("playbooks_latest") or "暂无（待日常反思补充）",
        "active_blockers": open_line,
    }

    if args.confirm_publish:
        card_updated = update_partner_card_pulse(
            args.card, ledger.get("playbooks_latest", ""), open_line
        )
        result["partner_card_updated"] = card_updated
        if card_updated:
            result["public_index_sync"] = sync_to_public_index(
                args.registry_doc, args.card, args.state
            )
    else:
        result["published"] = False
        result["publish_note"] = "Saved locally only. Re-run with --confirm-publish after member approves public_preview."

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
