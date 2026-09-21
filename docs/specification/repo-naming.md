---
tags: [已阅]
date: 2026-09-22
---

# 命名规范

## 规则总览

本规范只约束仓库、目录和资产类型命名，目标是让路径直接表达组织、领域、资产类型和内容职责。  

| **标识** | **硬约束** |
|:--|:--|
| ❗ 命名字符 | 仓库名和机器目录统一使用小写英文、数字和连字符，不使用空格、下划线或大小写混排 |
| ❗ 领域标识 | 领域短名用于领域仓库，领域英文名用于 `-of-` 后的领域标识，二者不能混用 |
| ❗ 资产类型 | 只能使用标准名称，不能用临时缩写、团队昵称或同义词替代 |
| ❗ 目录层级 | 双九宫格目录只建立在领域第二大脑根目录下 |
| ❗ 变更入口 | `Context`（工作语境）是新观察、新问题和工作约束的默认入口 |
| ❗ 过时归档 | 失效但需要追溯的内容移入 `Archive`（工作归档） |
| ❗ 改名同步 | 改名后必须同步更新 README、内部链接、CI 配置和依赖引用 |
| ❗ 新增类型 | 新增资产类型前，先确认现有类型无法表达该语义 |
| ❗ 资产治理 | 资产类型是命名、目录和文档格式的基础契约；九宫格中的资产类型变更必须先审议，并由资产治理团队维护 |

## 资产分类

`docs/` 目录下的程序型记忆回答“怎么做事”：约束层级分为宪法、法律、法理；消费对象分为人类、AI、规则引擎。  

| **约束层级** | **人类友好** | **AI 友好** | **规则引擎友好** |
|:--|:--|:--|:--|
| 宪法 | Bylaw（工作章程） | Specification（工程标准） | Toolkit（工具箱） |
| 法律 | Handbook（工作手册） | Gallery（工作案例） | Platform（平台） |
| 法理 | Tutorial（工作教程） | Essay（工作札记） | Example（示例程序） |

`data/` 目录下的陈述型记忆回答“知道什么”：类型分为事件、语义、自我；时间分为过去、现在、未来。  

| **时间维度** | **事件类** | **语义类** | **自我类** |
|:--|:--|:--|:--|
| 过去 | Report（工作报告） | Library（工作参考） | History（工作历史） |
| 现在 | Journal（工作日志） | Profile（工作档案） | Brochure（宣传册） |
| 未来 | Roadmap（路线图） | Insight（工作洞察） | Intention（工作意图） |

## 仓库命名

| **仓库类型** | **命名模板** | **示例** |
|:--|:--|:--|
| 领域第二大脑 | `quanttide-{领域短名}` | `quanttide-agent` |
| 资产第二大脑 | `quanttide-{资产类型}` | `quanttide-journal` |
| 资产交点 | `quanttide-{资产类型}-of-{领域英文名}` | `quanttide-journal-of-crowd-sourcing` |
| 法人主体资产 | `quanttide-{资产类型}-of-business-entity` | `quanttide-profile-of-business-entity` |
| Toolkit | `quanttide-{领域短名}-toolkit` | `quanttide-crowd-toolkit` |
| Platform | `qt{产品名}` 或 `qtcloud-{产品名}` | `qtcloud-learn` |
| Example | `quanttide-laboratory-of-{领域英文名}` | `quanttide-laboratory-of-crowdsourcing-management` |

## 目录结构

### 领域仓库

```text
quanttide-{领域短名}/
├── apps/          # Platform（平台）
├── packages/      # Toolkit（工具箱）
├── examples/      # Example（示例程序）
├── data/          # 陈述型记忆
│   ├── context/   # Context（工作语境）
│   ├── journal/   # Journal（工作日志）
│   ├── profile/   # Profile（工作档案）
│   ├── roadmap/   # Roadmap（路线图）
│   ├── insight/   # Insight（工作洞察）
│   ├── intention/ # Intention（工作意图）
│   ├── report/    # Report（工作报告）
│   ├── library/   # Library（工作参考）
│   ├── history/   # History（工作历史）
│   ├── brochure/  # Brochure（宣传册）
│   └── archive/   # Archive（工作归档）
└── docs/          # 程序型记忆
    ├── bylaw/          # Bylaw（工作章程）
    ├── specification/  # Specification（工程标准）
    ├── handbook/       # Handbook（工作手册）
    ├── gallery/        # Gallery（工作案例）
    ├── tutorial/       # Tutorial（工作教程）
    └── essay/          # Essay（工作札记）
```

### 资产仓库

```text
quanttide-{资产类型}/
├── default/       # 法人主体资产
└── domains/       # 各领域资产
    ├── {领域短名}/
    └── ...
```

### 目录职责

| **目录** | **固定资产** | **放置内容** |
|:--|:--|:--|
| `apps/` | Platform（平台） | 应用代码，可运行的产品、服务和部署单元 |
| `packages/` | Toolkit（工具箱） | 可被多个应用复用的工具、库和组件 |
| `examples/` | Example（示例程序） | 教学、验证和最小可运行示例 |
| `docs/` | Bylaw、Specification、Handbook、Gallery、Tutorial、Essay | 规则、标准、手册、案例、教程和札记 |
| `data/` | Context、Journal、Profile、Roadmap、Insight、Intention、Report、Library、History、Brochure、Archive | 工作语境、记录、档案、计划、认知和归档 |
