---
tags: [待审]
date: 2026-09-22
---

# Git 工作流

## Git 基础知识

### 名词释义

- fork：将别人的仓库复制到自己的仓库，以实现独立更改，未来可通过 PR 参与项目代码贡献
- ISSUE：用于发起对项目代码的讨论、反馈、建议等，类似论坛帖子，常用来在正式 PR 前进行初次沟通，减少协作摩擦
- PR：Pull Request 的简写，拉取请求，用于发起将个人本地 fork 的代码提交到他人远程仓库的申请

### 文件状态

- 工作区：本地文件，IDE 中所见即所得
- 暂存区：哪些文件的改动将参与下一次提交
- 版本库：已经提交的（版本）记录

### 常用命令

```bash
git clone <URL>.git # 从远程仓库克隆到本地
git clone --recurse-submodules <URL> # 从远程父子仓库克隆到本地

git status        # 查询本地分支与改动，绿色已暂存
git branch        # 查询本地全部分支

git checkout <分支名>     # 切换分支
git checkout main        # 切到主分支
git checkout -b <分支名>  # 基于当前位置，创建并切换分支

git add .         # 加入暂存区
git commit -m "前缀(范围): 中文简述" # 本地提交
git push          # 推送远程

git pull          # 当前分支的远程内容同步到本地 = fetch + merge
git fetch         # 获取信息：拉取不合并
git diff          # 查看不同
git merge <分支名> # 把 xxx 分支合并到当前分支
```

## 完整 PR 流程

- [ ] 1. [注册 GitHub 账号](https://github.com/signup)
- [ ] 2. [下载 GitHub Desktop](https://desktop.github.com/download/)
- [ ] 3. 在网页端打开目标仓库 URL，进入仓库首页，点击右上角的「Fork」
- [ ] 4. 


| 前缀          | 用途         |
| ----------- | ---------- |
| `feat/`     | 新功能        |
| `fix/`      | 修 bug      |
| `docs/`     | 文档变更       |
| `chore/`    | 杂务（配置、依赖等） |
| `refactor/` | 重构         |

- 分支名 = 前缀/描述：描述用英文小写，单词间用 `-` 连接
- 默认推送和拉取同名分支；合进主干走 PR，不要把功能分支直接推到 main