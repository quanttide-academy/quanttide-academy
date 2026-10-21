# AGENTS.md

本文是 AI 在本仓库工作的刚性规范与上下文入口，每次接任务前先读。冲突时本文优先；命名与目录以 [second-brain.md](./docs/specification/second-brain.md) 为准。  
多人异步协作，改动经 PR 合并入 `main`。  

## 项目概述

量潮实训基地的领域级第二大脑（`quanttide-academy`）。存放量潮实训基地的文档（规章、工程规范、教程）及可复用工具，承接实训基地的多人异步协作工作。  

## 相关文档

- [README.md](./README.md)：推荐人类阅读与了解本项目的入口

## 快速定位

| **关键词** | **文件** | **锚点** |
| :-- | :-- | :-- |
| 章程、组织架构、岗位职责 | [index.md](./docs/bylaw/index.md) | 第四章 组织架构与岗位职责 |
| 沟通、周会 | [index.md](./docs/bylaw/index.md) | 第五章 工作生态（第二十条 沟通原则） |
| 命名、目录、资产类型 | [second-brain.md](./docs/specification/second-brain.md) | 规则总览；资产分类；目录结构 |
| 写章程 | [bylaw.md](./docs/specification/bylaw.md) | 第二章 文档结构 |
| Git、PR | [git-workflow.md](./docs/tutorial/git-workflow.md) | 完整 PR 流程 |
| 飞书、待办、群聊、watch、org | [AGENTS.md](./packages/quanttide-academy-toolkit/AGENTS.md) | 常见任务；工作流程 |

## 业务意图

为量潮科技及量潮创新联盟其他成员输送合格实习生。实训基地作为量潮的影子公司，以最低运营成本自组织、自进化。  

## 关键决策

1. **第二大脑结构**：仓库按领域第二大脑组织，`docs/` 存程序型记忆，路径直接表达资产类型
2. **命名契约**：仓库名和目录统一用小写英文、数字和连字符，资产类型只用标准名称
3. **人机分入口**：README 面向人类阅读，AGENTS.md 面向 AI 执行，二者互不抄写
4. **工具内置**：可复用 skill 放 `.agent/skills/`，Markdown 格式由 `markdown-editor` 统一

## 项目目录

```text
quanttide-academy/
├── README.md
├── AGENTS.md
├── .gitignore
├── docs/                              # 程序型记忆
│   ├── bylaw/                         # Bylaw（工作章程）
│   ├── specification/                 # Specification（工程标准）
│   └── tutorial/                      # Tutorial（工作教程）
├── packages/                          # Toolkit（可复用工具包）
│   └── quanttide-academy-toolkit/     # 实训基地工具箱（飞书工作流子模块）
└── .agent/
    └── skills/                        # Toolkit（工作所需 skill 与脚本）
        ├── agents-editor/             # 撰写、重构 AGENTS.md
        ├── create-skill/              # 编写、审核 skill
        ├── feishu-workflows/          # 飞书工作流引导
        ├── issue-editor/              # 撰写 GitHub Issue
        ├── markdown-editor/           # Markdown 笔记规范
        ├── pr-editor/                 # 撰写 PR 标题与描述
        └── readme-editor/             # 撰写、重构 README
```

## 关键文件

| **文件** | **职能** |
| :-- | :-- |
| [second-brain.md](./docs/specification/second-brain.md) | 命名与目录规范，新增或改名路径的落点依据 |
| [index.md](./docs/bylaw/index.md) | 实训基地工作章程 |
| [markdown-editor](./.agent/skills/markdown-editor/SKILL.md) | 写、改 Markdown 笔记时的格式规范 |
| [agents-editor](./.agent/skills/agents-editor/SKILL.md) | 撰写、重构本文时的模板与验收清单 |

## 核心原则

- 最小干预：仅在用户明确请求时改文件，不主动改无关文件
- 用到再建：除本树已有路径和 README、AGENTS.md 这类根契约外，不创建未使用的文件或九宫格目录
- 结构同步：改名或变更目录后，README「仓库结构」、本文「项目目录」「快速定位」与内部链接必须同一轮改完
- 技能优先：动手前先查 `.agent/skills/`；已有 skill 或工具能做的，禁止另写脚本
- 最大兼容：优先 GFM / CommonMark / LaTeX，不用编辑器私有语法
- 信息复用：不把 handbook、specification、skill 正文抄进其他文件，用相对链接

## 工作流程

按编号顺序执行，未触发的步骤跳过，已触发的步骤做完才进入下一步，禁止跳步、并步。  

1. 理解需求：明确请求范围，只改被要求的文件
2. 查契约：读 README 确认入口；新增或改名路径时，读 second-brain.md 确认落点
3. 匹配技能：写笔记用 `markdown-editor`，改 README 用 `readme-editor`，改本文用 `agents-editor`，写 skill 用 `create-skill`，写 Issue 用 `issue-editor`，写 PR 用 `pr-editor`，飞书工作流用 `feishu-workflows`，命中则先读再动手
4. 检查现状：新建路径时，确认目标路径是否已存在，不预建未使用的目录
5. 执行操作：skill 放 `.agent/skills/{skill 名}/`；已有正文用相对链接，不抄写
6. 结构同步：改名或变更目录时，同一轮更新 README「仓库结构」、本文「项目目录」「快速定位」与内部链接
7. 验证结果：按验证清单逐条核对，失败不得交付

## 安全约束

- 禁止读取 `.env` 等密钥文件内容，禁止把密码、密钥、令牌、邮箱口令写入仓库文件、日志或协作材料（设计、截图、视频、任务页）
- 发现明文凭据时停止写入，提醒用户轮换，不在回复中复述秘密内容
- 用户明确要求时才提交或推送
- 只改用户明确提到的工作范围内的文件；范围外的文件须先征得用户同意再改
- 用户有决定权的内容（如任务勾选与评审结论）禁止擅自修改或打勾

## Cursor Cloud specific instructions

可运行代码在子模块 `packages/quanttide-academy-toolkit`。环境 install 会初始化该子模块，把 `uv` 0.13.4 与 `lark-cli` 1.0.98 链到 `/usr/local/bin`，并在子模块执行 `uv sync --frozen --python 3.12`。测试与自检在子模块目录执行，命令见 [AGENTS.md](./packages/quanttide-academy-toolkit/AGENTS.md)「常用命令」。

飞书登录要本人扫码，不放进 install。没有 `config.yaml` 时 `uv run feishu-workflows doctor --json` 退出码为 1，并指向 `feishu-workflows-setup questions --json`。离线闭环用 `uv run feishu-workflows selftest --json`。

`tests/fixtures/topics.json` 第 2 条截止日期是 `2026-10-23`。从 2026-10-21 起，该条落入「截止在 2 天内，优先级至少 P2」规则，真实时钟下 `selftest` 与一部分 `pytest` 会失败。把时钟设到 2026-10-15 时，`uv run pytest -q --cov` 为 231 passed、覆盖率 91%，`selftest` 为 `"status": "ok"`，`integrated_tests/core/test_migrations.py` 与 `integrated_tests/watch/test_poll.py` 为 2 passed，`ruff check` 与 `ruff format --check` 通过。

## 验证清单

- [ ] 1 只改了用户明确请求的文件
- [ ] 2 新增或改名路径已按 second-brain.md 确认落点
- [ ] 3 已按命中的 skill 执行；Markdown 笔记 frontmatter 为 `tags: [...]` + `date: YYYY-MM-DD`
- [ ] 4 未创建未使用的文件或九宫格目录
- [ ] 5 未使用编辑器私有语法；未抄写 handbook、specification、skill 正文；内部链接指向已存在文件
- [ ] 6 改名或变更目录后，README「仓库结构」、本文「项目目录」「快速定位」与内部链接已同一轮更新
