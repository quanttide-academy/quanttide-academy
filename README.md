---
tags: [已阅]
date: 2026-09-22
---

# 量潮实训

本仓库存放量潮实训基地的文档（规章、任务清单、工程规范）及可复用工具，承接实训基地的多人异步协作工作。  

## quick-start

建议按如下顺序阅读：  

1. [了解量潮科技](https://strategy.quanttide.com/)
2. [量潮科技代码仓库](https://github.com/quanttide)
2. [了解实训基地](./docs/bylaw/实训基地章程.md)
3. [实训基地代码仓库](https://github.com/quanttide-academy/quanttide-academy)
3. 学习 Markdown 语法（未写入 
4. [学习 Git 工作流（待完善）](./docs/tutorial/git-workflow.md)
5. 学习如何使用 Cursor（未写入）
6. 明确本仓库结构
   - [仓库结构](#仓库结构)
   - [仓库命名规范](./docs/specification/repo-naming.md)
7. [如何领取任务](./roadmap.md) 
8. [如何发布任务](./docs/handbook/co-guide.md#发布任务)
9. [完整协作流程（待打磨）](./docs/handbook/co-guide.md)

也可以在 AI 的对话窗口复制粘贴如下提示词，快速理解学习本仓库内容：  

```markdown
你是一个资深的软件工程师，我是一个编程小白，基于本项目全部已有文件，带我一步步从工具下载、注册、乃至环境搭建，了解并熟悉这个项目，要求如下：
1. 每次只指引我做一小步
2. 每个步骤可以看到即时验收成果
```

## 仓库结构

```text
quanttide-training/
├── README.md                        # 人类阅读入口
├── AGENTS.md                        # AI 工作指南
├── roadmap.md                       # 任务清单
├── .gitignore
├── docs/
│   ├── bylaw/
│   │   └── 实训基地章程.md            # 工作章程
│   ├── handbook/
│   │   └── co-guide.md              # 协作流程
│   ├── specification/
│   │   ├── repo-naming.md           # 仓库命名规范
│   │   └── roadmap-template.md      # 任务清单规范
│   └── tutorial/
│       └── git-workflow.md          # Git 工作流
└── .agent/                          # 可复用工具
    └── md-writer/
        └── SKILL.md
```
