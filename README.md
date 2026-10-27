# 量潮实训

本仓库存放量潮实训基地的文档（规章、工程规范、教程、工作报告）及可复用工具，承接实训基地的多人异步协作工作。  

## quick-start

建议按如下顺序阅读：  

1. [了解量潮科技](https://strategy.quanttide.com/)
2. [量潮科技代码仓库](https://github.com/quanttide)
3. [了解实训基地及其工作章程](./docs/bylaw/index.md)
4. [实训基地代码仓库](https://github.com/quanttide-academy/quanttide-academy)
5. 明确本仓库结构
   - [仓库结构](#仓库结构)
   - [命名规范](./docs/specification/second-brain.md)
6. 学会使用仓库工具：动手前让 AI 先读对应 skill 再执行

   | **场景** | **skill** | **用途** |
   | :-- | :-- | :-- |
   | 写、改 Markdown 笔记 | [markdown-editor](./.agent/skills/markdown-editor/SKILL.md) | 统一排版格式 |
   | 写、改 README | [readme-editor](./.agent/skills/readme-editor/SKILL.md) | 只改过期的节 |
   | 写、改 AGENTS.md | [agents-editor](./.agent/skills/agents-editor/SKILL.md) | 模板与验收清单 |
   | 新建或审核 skill | [create-skill](./.agent/skills/create-skill/SKILL.md) | skill 结构与写法 |
   | 复杂任务需协作，提 PR 前沟通 | [issue-editor](./.agent/skills/issue-editor/SKILL.md) | 标题与正文模板 |
   | Issue 沟通完成后提交代码 | [pr-editor](./.agent/skills/pr-editor/SKILL.md) | 标题与描述模板 |
   | 飞书群聊待办、人员跟踪与群管理 | [feishu-workflows](./.agent/skills/feishu-workflows/SKILL.md) | 实训基地工具箱的当前通道（飞书协作接驳） |

7. 周会简报
   - 编撰：先读 [周会简报版式](./docs/specification/weekly-brief.md)，再写入 [data/report/weekly-brief/](./data/report/weekly-brief/)
   - 查询过往：打开 [data/report/weekly-brief/](./data/report/weekly-brief/)
8. 学习如何使用 Grok Bot + Cursor（未写入）
9. [学习 Git 工作流（待完善）](./docs/tutorial/git-workflow.md)

也可以将本仓库作为上下文投喂给 AI，并在 AI 的对话窗口复制粘贴如下提示词，快速理解学习本仓库内容：  

```markdown
你是一个资深的软件工程师，我是一个编程小白，基于本项目全部已有文件，带我一步步从工具下载、注册、乃至环境搭建，了解并熟悉这个项目，要求如下：
1. 每次只指引我做一小步
2. 每个步骤可以看到即时验收成果
```

## 仓库结构

```text
quanttide-academy/
├── README.md                        # 人类阅读入口
├── AGENTS.md                        # AI 工作指南
├── .gitignore
├── docs/
│   ├── bylaw/
│   │   └── index.md                 # 工作章程
│   ├── specification/
│   │   ├── bylaw.md                 # 章程写作章程
│   │   ├── proposal.md              # 提案写作规范
│   │   ├── second-brain.md          # 命名规范
│   │   └── weekly-brief.md          # 周会简报版式
│   └── tutorial/
│       └── git-workflow.md          # Git 工作流
├── data/
│   └── report/
│       └── weekly-brief/            # 周会简报
├── packages/
│   └── quanttide-academy-toolkit/   # 实训基地工具箱（当前通道：飞书协作接驳）
└── .agent/                          # skill
```
