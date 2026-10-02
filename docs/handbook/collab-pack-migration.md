---
tags: [待审]
date: 2026-10-02
---

# 协作包迁移说明（product-requirement-loop → 本仓）

## 结论摘要

| 项 | 状态 |
|----|------|
| 产品安全门禁 `verify_security` | 本地 30/30 PASS |
| 踩坑回归 `verify_lessons` | 本地 27/27 PASS |
| 文档布局 `verify_docs_layout` | 本地 33/33 PASS |
| 主分支 CI「Strict delivery + security gates」 | success |
| 企业级 PR 套件（classify/delivery/scope/lock/reviewers） | 已迁入本仓工作流 |
| 真人必审三票跑通 | 仍待学院仓实跑 |
| 任务 Issue 从产品仓迁出 | 进行中（先迁模板与流水，再逐条建 Issue） |

## 迁了什么

- `.github/workflows/`：task-board、required-reviewers、enterprise-pr、pr-task-gate、pr-ai-checklist、task-stale-release
- `.github/ISSUE_TEMPLATE/task.yml`、`PULL_REQUEST_TEMPLATE/*`
- `scripts/pr_delivery_check.py`、`scripts/pr_scope_guard.py`
- `docs/designs/_TEMPLATE.md`
- handbook：enterprise-pr / reviewer-guide / trainee-collab / task-issue-block

## 没迁什么（有意）

- 产品业务代码与产品专用 `ci.yml`（仍留在 `hongwei-2026/product-requirement-loop`）
- 产品仓既有任务 Issue #1–#22（需在本仓按 roadmap 重建或链接）

## 关联 Issue

- https://github.com/quanttide-academy/quanttide-academy/issues/4

## 请负责人确认

@Guo-Zhang 请审本 PR：协作 Issue/PR 是否以本仓库为准；工作流是否可开。
抄送审核员：@Jerrybao99 @hl019 @likexin105 @hongwei-2026
