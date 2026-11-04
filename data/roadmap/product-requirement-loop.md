---
tags: [roadmap, platform]
date: 2026-11-02
---

# product-requirement-loop（平台项目）

## 基本信息

- 发起人：于鸿伟
- 发起日期：26-09-22
- 项目描述：把官方产品日志整理成需求故事与定稿 JSON，供产品同事审阅。
- 产品代码仓：[hongwei-2026/product-requirement-loop](https://github.com/hongwei-2026/product-requirement-loop)
- 同事唯一入口（产品仓）：[`docs/handbook/index.md`](https://github.com/hongwei-2026/product-requirement-loop/blob/main/docs/handbook/index.md)
- 开发者协作（产品仓）：[`docs/handbook/developer-collaboration.md`](https://github.com/hongwei-2026/product-requirement-loop/blob/chore/align-package-layout/docs/handbook/developer-collaboration.md)

## 与实训基地工具包对齐

产品仓目录已对齐本仓 [`packages/quanttide-academy-toolkit`](../../packages/quanttide-academy-toolkit) 约定：

| 项 | 产品仓路径 |
| :-- | :-- |
| Python 包 | `src/product_requirement_loop/` |
| 测试 | `tests/` |
| 包元数据 | `pyproject.toml` |
| Agent 约束 | `AGENTS.md` |
| 环境模板 | 根目录 `.env.example` → 复制到 `project/.env` |
| 运行时数据 | `project/`（日志库、`.env`、启动脚本） |

## 当前交付（学院侧跟踪）

| 项 | 链接 |
| :-- | :-- |
| 产品 Issue | [#27 开发者协作指南与 packages 结构对齐](https://github.com/hongwei-2026/product-requirement-loop/issues/27) |
| 产品 PR | [#28 Impl #27](https://github.com/hongwei-2026/product-requirement-loop/pull/28) |

## 协作说明

- 任务认领、Design / Impl、门禁与 `/approve` 流程以**产品仓 handbook** 为准；本文件只做学院总览索引，不重复细则。
- 文档 / 结构类评审通知：**@hl019（黄亮）**；**勿 @Guo-Zhang**（不负责本产品任务审阅）。
- 难做、需多人协作的任务才在 roadmap 登记；基础修复在产品仓自行完成。

## 验收标准（项目级）

- [ ] 产品仓 handbook 为唯一同事入口
- [ ] 新同学可按 developer-collaboration 完成 clone → env → pytest → 提 PR
- [ ] 目录与工具包约定一致且 CI 测试通过
