# AGENTS.md

## 相关文档

- [README.md](./README.md)：推荐人类阅读与了解本项目的入口

## 项目概述

量潮实训基地的领域级第二大脑（`quanttide-academy`）。存放量潮实训基地的文档（规章、任务清单、工程规范）及可复用工具，承接实训基地的多人异步协作工作。 

## 项目目录

```text
quanttide-academy/
├── README.md
├── AGENTS.md
├── roadmap.md
├── .gitignore
├── docs/                              # 程序型记忆
│   ├── bylaw/                         # Bylaw（工作章程）
│   │   └── index.md
│   ├── handbook/                      # Handbook（工作手册）
│   │   └── co-guide.md
│   ├── specification/                 # Specification（工程标准）
│   │   ├── bylaw.md
│   │   ├── roadmap.md
│   │   └── second-brain.md
│   └── tutorial/                      # Tutorial（工作教程）
│       └── git-workflow.md
└── .agent/                            # Toolkit（工作所需 skill 与脚本）
    └── skills/
        ├── agents-editor/
        │   └── SKILL.md
        ├── markdown-editor/
        │   └── SKILL.md
        └── pr-editor/
            └── SKILL.md
```

## 核心原则

- **最小干预**：仅在用户明确请求时改文件，不主动改无关文件
- **用到再建**：除本树已有路径和 README、AGENTS.md 这类根契约外，不创建未使用的文件或九宫格目录
- **结构同步**：改名或变更目录后，README「仓库结构」、本文「项目目录」与内部链接必须同一轮改完
- **最大兼容**：优先 GFM / CommonMark，不用编辑器私有语法
- **信息复用**：不把 handbook、specification、skill 正文抄进其他文件，用相对链接

## 工作流程

1. **理解需求**：明确请求范围，只改被要求的文件
2. **查契约**：读 README 确认入口；读 `docs/specification/second-brain.md` 确认落点
3. **检查现状**：目标路径是否已存在；不预建未使用的目录
4. **执行操作**：工具放 `.agent/skills/{工具短名}/`；已有正文用相对链接，不抄写
5. **结构同步**：若改名或变更目录，同一轮更新 README「仓库结构」、本文「项目目录」与内部链接
6. **验证结果**：按下方清单逐项核对

## 验证清单

- [ ] 只改了用户明确请求的文件
- [ ] 未创建未使用的文件或九宫格目录
- [ ] 新增或改名路径已按 `docs/specification/second-brain.md` 确认落点
- [ ] Markdown 笔记 frontmatter 为 `tags: [...]` + `date: YYYY-MM-DD`
- [ ] 未使用编辑器私有语法
- [ ] 未抄写 handbook、specification、skill 正文；内部链接指向已存在文件
- [ ] 改名或变更目录后，README「仓库结构」、本文「项目目录」与内部链接已同一轮更新

## 安全约束

- 禁止将密码、密钥、令牌、邮箱口令写入仓库任何文件
- 协作材料（设计、截图、视频、任务页）同样不得包含密钥
- 发现明文凭据时停止写入，提醒用户轮换，不在回复中复述秘密内容
