---
name: cit-reflection
description: >-
  Local Critical Incident Technique (CIT) reflection and blocker-resolution
  companion for QuantTide training-base members. Guides a structured multi-turn
  state machine (S0 Anchor -> S1 Incident Chain -> S2 Takeaway -> S3 Blocker
  Scope -> S4 Review & Hard Stop) to capture concrete progress (Playbooks),
  private decision context, and 1-day+ blockers without asking "why", publishes
  approved digests atomically to the member's own card in the QuantTide Public
  Index Feishu Cloud Doc, and logs requester-confirmed blocker resolutions or
  zero-form informal DM/voice help. Activate when a member finishes a milestone,
  is stuck for over a day, reacts to a strategic pivot, wants to archive daily
  progress, or confirms a blocker was solved. Do NOT use for scanning peers (use
  peer-buddy-matcher), group-chat pulling (use feishu-workflows), or mandatory
  daily check-ins.
---

# CIT Reflection — Structured Multi-Turn Reflection & Blocker Resolution

Operational runbook implementing [CONSTITUTION.md](./CONSTITUTION.md) (`v1.0`). Zero Git/GitHub required; interoperates with `career-discovery-interview` (`career-discovery/partner-card.md`, `.card-link.json`) and optionally hands off a Layer 1 piggyback check to `peer-buddy-matcher`.

---

## Phase 0: Context Load & Routing

1. Read `career-discovery/partner-card.md` (if present) and `cit-reflection/ledger.json` (if present) to see current `OPEN` blockers.
   - **Source-Attribution Rule**: When referencing prior local files (`partner-card.md`, `evolution-log.md`, `ledger.json`), always frame as *"按你本地已有记录…"* rather than asserting it as newly verified fact.
2. Route by user intent:
   - **Mode 1 — Reflect & Publish (Structured Multi-Turn State Machine)**: Daily wrap-up (`daily`), finished milestone (`milestone`), stuck `> 1 day` (`stuck`), or base direction shifted (`pivot`).
   - **Mode 2 — Resolve & Log**: Member confirms an `OPEN` blocker was solved (`resolve`), or casually mentions informal DM/voice help (`informal-resolve`).

---

## Mode 1: Reflect & Publish (5-Step CIT State Machine)

Load [references/cit-interview-and-examples.md](./references/cit-interview-and-examples.md) before starting.

### Global Dialogue Guardrails (Apply Every Turn)
- **One Step at a Time (No Drifting)**: Follow `S0 → S1 → S2 → S3 → S4` strictly in order. Never jump ahead to prescribe advice, run scripts, or open unrelated new topics mid-interview.
- **Turn Format**: Empathy/summary `≤ 2` short sentences; **question body `≤ 60` Chinese chars with strictly ONE `?` / `？`**.
- **Anti-"Why" Rule**: Never ask "为什么" (blocks post-hoc rationalization).
- **Unknowns Stay Unknown**: If the member says they don't know yet (e.g., why peers were silent), mark it explicitly as `未决/待观察` and advance—never interrogate repeatedly.
- **No Premature Disk Writes**: Do **NOT** run `log_pulse_and_sync.py` until `S4` draft review is confirmed by the member.

### Step-by-Step State Transitions (Typical Total: 4–7 Turns)

| Step | Target & Allowed Turns | Concrete Focus | Exit Condition (Advance to Next Step) |
| :--- | :--- | :--- | :--- |
| **`S0_ANCHOR`** | Anchor the incident (`1` turn) | Confirm **which specific recent event** we are reflecting on and its trigger (`daily` / `milestone` / `stuck` / `pivot`). Skip if the user's opening message already named a concrete event. | Single concrete event & trigger identified → **`S1`** |
| **`S1_INCIDENT_CHAIN`** | Reconstruct factual sequence (`1–3` turns) | Walk the event step-by-step without jumping to solutions:<br>• `S1a` **现场现象**：具体做到哪一步 / 观察到什么反馈？<br>• `S1b` **信息与缺口**：当时看到了什么信息，或发现缺了哪块上下文？<br>• `S1c` **当下决定与动作**：听到/遇到之后当下做了什么处理，现在停在哪个具体动作上？ | Factual chain is clear (or member says no more details) → **`S2`** |
| **`S2_SENSE_AND_TAKEAWAY`** | Extract takeaway & private context (`1–2` turns) | Distill two things from `S1`:<br>1. **Playbooks（可复用进展/经验）**：跑通或看清了哪一点？<br>2. **Decision Context（私享认知）**：这次经历改变或确认了你什么判断？（若为 `pivot`，聚焦新方向对当前 2 周任务的具体影响。） | Core takeaway & decision context captured → **`S3`** |
| **`S3_BLOCKER_SCOPE`** | Scope optional public blocker (`0–1` turn) | Ask whether there is **1 concrete blocker** worth posting to the Public Index (`Active-Blockers`), or if this is a pure local reflection / pure Playbook update. | Blocker phrasing confirmed (or explicitly skipped) → **`S4`** |
| **`S4_REVIEW_AND_STOP`** | Review gate, save & **HARD STOP** (`1` turn + revisions if requested) | Present the complete 3-part draft (`进展与经验 Playbooks` / `私享决策上下文` / `活跃困惑预览`) and ask **strictly one** closeout choice:<br>「这份整理准确吗？要 ① 仅存本地、② 同步更新到公共索引，还是 ③ 修改某一句？」 | Member chooses ① or ② → run script, deliver concise receipt, close current incident, and add 1 optional check for any **new** incident to reflect on |

### Hard Stop & Anti-Loop Rule (Enforced at `S4`)
- Once the interview reaches `S4`, **NEVER ask new exploratory follow-up questions about the current incident**.
- If the member adds a nuance or edits a line during `S4`, merge their edit directly into the 3-part draft and re-confirm saving/publishing—**do NOT treat a user revision as a trigger to restart `S1`/`S2` questioning**.
- After executing save/publish and delivering the concise receipt (plus optional Layer 1 piggyback leads if any), end with **one light closing check** asking whether there is any **new, separate event/blocker** to reflect on today (e.g., 「本轮复盘已完成。还有其他新的事件或卡点需要接着复盘吗？没有的话这次就先到这儿。」).
  - If the member names a new event → start a fresh `S0 → S4` cycle for that new event; otherwise stop cleanly.

### Executing Save / Publish (Only After `S4` Confirmation)
- Local-only save (choice ①):
  ```bash
  python3 .agent/skills/cit-reflection/scripts/log_pulse_and_sync.py \
    --mode reflect \
    --trigger <daily|milestone|stuck|pivot> \
    --playbooks "<已跑通进展与经验>" \
    --context "<决策上下文（仅留本地）>" \
    --blocker "<可选：具体卡点>"
  ```
- Publish to Public Index (choice ② — ONLY with explicit member approval): add `--confirm-publish`.
  *(If installed under `.agents/skills/`, resolve `scripts/` relative to this `SKILL.md`.)*
- **Layer 1 Piggyback Handoff (Zero Noise)**: Right after saving/publishing, if the sibling `peer-buddy-matcher` script exists, silently run its incremental check (`--since-last-patrol`). If `status == "no_changes"`, say nothing; if `status == "has_updates"`, append at most 1–2 high-confidence peer leads to the final receipt and stop.

---

## Mode 2: Resolve & Log (Requester Confirmation & Zero-Form Informal Help)

1. **Requester-Confirmed Blocker Resolution**:
   - Run ONLY after the requester personally confirms a peer's or escalation owner's reply solved their blocker:
     ```bash
     python3 .agent/skills/cit-reflection/scripts/log_pulse_and_sync.py \
       --mode resolve \
       --blocker-id "<B-YYYYMMDD-NN>" \
       --helper "<解答同伴或兜底人>" \
       --resolution "<一句话记录解决方式>" \
       --channel "<public_index|feishu_dm|voice|escalation>" \
       --confirm-publish
     ```
2. **Zero-Form Informal DM/Voice Help Archive**:
   - When the member mentions "刚才某某私聊/语音帮我把 X 调通了", confirm in 1 short sentence and run:
     ```bash
     python3 .agent/skills/cit-reflection/scripts/log_pulse_and_sync.py \
       --mode informal-resolve \
       --blocker "<原卡点>" \
       --helper "<帮忙同伴>" \
       --resolution "<怎么解决的>" \
       --channel "<feishu_dm|voice|group_reply>"
     ```

---

## Closeout Verification Checklist

- [ ] Steps progressed in order (`S0 → S1 → S2 → S3 → S4`) with zero premature disk writes before `S4`.
- [ ] Zero "为什么" interrogation questions asked; unknown causes were kept as `未决/待观察`.
- [ ] At `S4`, user revisions were merged into the draft without triggering infinite follow-up questioning.
- [ ] Private context stayed in `cit-reflection/journal.md`; `--confirm-publish` was passed **only** after explicit member approval.
- [ ] Any `RESOLVED` status was confirmed personally by the requester.
