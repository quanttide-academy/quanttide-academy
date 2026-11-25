---
name: peer-buddy-matcher
description: >-
  Host-agnostic Peer-Buddy matching skill for QuantTide training-base members.
  Patrols the QuantTide Public Index Feishu Cloud Doc to surface high-confidence
  bidirectional leads — Supply leads (peers whose OPEN blockers match your
  strengths/Playbooks) and Demand leads (peers who can unblock you or co-run a
  2-week MVP) — with ready-to-paste Feishu DM icebreakers. Supports Layer 0
  on-demand scans and Layer 1 zero-noise incremental piggyback checks
  (--since-last-patrol) after cit-reflection or feishu-workflows so any local AI
  client (Codex, WorkBuddy, Cursor, Claude Code) stays silent when nothing
  changed. Activate when a member asks to find partners, check who needs help,
  or runs a post-reflection/post-digest incremental check. Do NOT use for
  logging your own reflection (use cit-reflection), pulling group chats (use
  feishu-workflows), or auto-sending Feishu DMs.
---

# Peer-Buddy Matcher — Incremental Public Index Patrol & Bidirectional Matching

Host-agnostic matching runbook. Works identically across Codex, WorkBuddy, Cursor, Claude Code, and any local AI client via `lark-cli` (zero background daemon required).

---

## Trigger Layers (Progressive Proactivity)

- **Layer 0 (On-Demand)**: Member explicitly asks to scan the Public Index for partners or peers to help → run **full patrol** (omit `--since-last-patrol`).
- **Layer 1 (Incremental Piggyback — Zero Noise)**: Invoked right after `cit-reflection` or `feishu-workflows` → run with `--since-last-patrol`:
  - Compares per-peer content hashes against `career-discovery/.patrol-state.json` (ignores your own card edits so updating yourself never causes a false-positive self-trigger).
  - If `status == "no_changes"` → **stay completely silent** (zero interruption).
  - If `status == "has_updates"` → surface at most **1–2** high-confidence leads at the end of the reply, then advance the cursor with `--mark-seen`.

---

## Execution Workflow

1. **Load Local Member Context (Parallel)**:
   - Read `career-discovery/profile.md`, `career-discovery/partner-card.md`, and `cit-reflection/ledger.json` (if present) for the member's `Offer`, `Seek`, `Avoid`, `Playbooks`, and active `OPEN` blockers.
   - Load [references/matching-rubric-and-icebreakers.md](./references/matching-rubric-and-icebreakers.md).
2. **Run Public Index Patrol Script**:
   - **Layer 0 (On-Demand Full Scan)**:
     ```bash
     python3 .agent/skills/peer-buddy-matcher/scripts/patrol_public_index.py \
       --registry-doc W90qdp8azogcCZxCNGfcEEWonuc \
       --state career-discovery/.card-link.json \
       --sla-hours 48 \
       --mark-seen
     ```
   - **Layer 1 (Incremental Piggyback Check)**:
     ```bash
     python3 .agent/skills/peer-buddy-matcher/scripts/patrol_public_index.py \
       --registry-doc W90qdp8azogcCZxCNGfcEEWonuc \
       --state career-discovery/.card-link.json \
       --since-last-patrol \
       --sla-hours 48 \
       --mark-seen
     ```
     *(If installed under `.agents/skills/`, resolve `scripts/` relative to this `SKILL.md`.)*
3. **Evaluate & Filter Leads (Anti-Noise Cap)**:
   - In Layer 1: if `status == "no_changes"`, output nothing extra.
   - Otherwise, score candidates against the rubric in `references/matching-rubric-and-icebreakers.md`:
     - **Supply Leads（“这个问题我能顺手帮”）**: Peer's `OPEN` blocker directly matches member's `Offer` / `Playbooks` / `Q1` and does not violate `Avoid`.
     - **Demand Leads（“可向对方请教 / 临时搭伙”）**: Member's `OPEN` blocker or 2-week MVP directly matches peer's `Offer` / `Playbooks` / `Seek`.
   - **Strict Cap**: Present **at most 3 leads** in Layer 0 (**1–2** in Layer 1). If 0 candidates meet the concrete-match bar, state honestly: *"公共索引共扫描 N 位同伴，目前暂无与你当前任务强匹配的线索，无需打扰。"*
4. **Deliver Actionable Output (Never Auto-Send DMs)**:
   - For each surfaced lead, provide:
     1. 1-sentence concrete match reason;
     2. Peer's Bento homepage link (from `homepage_url`);
     3. A short, low-friction Feishu DM icebreaker draft ready to copy-paste.
   - If `overdue_self_blockers` is non-empty (`> 48h`), add one gentle reminder that the member may clarify reproduction details or escalate to the rotating secretariat / mentor.

---

## Closeout Verification Checklist

- [ ] Layer 1 `no_changes` produced zero noisy output.
- [ ] Surfaced leads respected the `≤ 3` (Layer 0) / `≤ 2` (Layer 1) cap and never padded weak generic overlaps.
- [ ] Zero Feishu DMs were auto-sent; only copy-paste drafts were provided.
