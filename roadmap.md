# 实训基地任务清单

本文档为量潮实训基地任务清单，用于记录和跟踪实训基地的日常任务和项目任务。 
项目优先级顺序：紧急重要 > 紧急次要 > 缓和重要 > 缓和次要  

## 日常任务：实训基地章程完善

- 优先级：紧急重要
- 文件位置：`docs/bylaw/index.md`
- 任务要求：
	- [ ] 组织架构、岗位职责、沟通渠道等较为模糊，建议进一步深化
	- [ ] 润色后加入到适宜位置：量潮实训基地的核心工作意图，是为量潮科技以及量潮创新联盟的其他成员提供合格的实习生。因为随着我们组织的进化，我们对于合格实习生的标准也越来越高；由于规模化的深入，我们所需要的人才密度也越来越高。所以，实训基地主要是用来承载这个目标所需要的合格实习生。
    - [ ] 添加`定期周会，周会定义为交流和学习的碰头会`进入工作章程适宜位置
    - [ ] 使用本项目内置 skill `markdown-editor`生成，确保排版符合量潮规范
- 参考资料：
	- [量潮工作章程模板](docs/specification/bylaw.md)
	- 量潮各仓库工作章程
- 咨询对象：果总、鲍宇航
- 执行员：
    - [ ] 林莉婷
- 评审员：王敏华 -> 鲍宇航
    - [ ] 王敏华
    - [ ] 鲍宇航
- 评审标准：
	- [ ] 任务要求全部满足
    - [ ] 文档可读性良好
    - [ ] 措辞正式、准确、简洁、清晰
	- [ ] 评审员按顺序评审通过
- DDL：
    - 林莉婷：26-
    - 王敏华：26-
    - 鲍宇航：26-

## 日常任务：增加项目管理章程

- 背景：目前课题主要是在个人账号管理，不具备作为实训基地内部身份的能力。因此建议有一个立项流程，把仓库转移到这个组织里。作为收益，这个项目被捐赠给组织以后，可以通过组织的名义分发任务。这样也更容易合规。
- 要求：
	- [ ] 和果总进一步接洽，理解并明确背景中其真实意图
	- [ ] 人员间自行分工合作完成
- 人员：王敏华、林莉婷
- DDL：

## 日常任务：agents-editor 的 skill 建设

- 要求：
	- [ ] 该 skill 加入 .agent 文件夹
	- [ ] 
	- [ ] 
- 人员：黄亮
- DDL：

- [ ] 任务：pr-editor 的 skill 建设
- 要求：
	- [ ] 该 skill 加入 .agent 文件夹
	- [ ] 适用于最广泛通用场景的 pr title 和 description 撰写 skill
- 人员：黄亮
- DDL：

- [ ] 任务：readme-editor 的 skill 建设
- 要求：
	- [ ] 该 skill 加入 .agent 文件夹
	- [ ] 刷新第二大脑仓库的 README.md
- 参考：agents-editor 的排版、格式、风格、要求
- 人员：
- DDL：

## 日常任务：添加福利激励制度

- [ ] 进入章程适宜位置
- [量潮当前福利激励制度](https://quanttide.feishu.cn/docx/GreedAGs8oiwT5xQVB8cykf1nbD)


## 项目任务：product-requirement-loop

### 基本信息

- 发起人：于鸿伟
- 发起日期：26-09-22
- 项目描述：把量潮官方产品日志整理成需求故事和定稿 JSON，供产品同事审阅。
- 验收标准：https://github.com/hongwei-2026/product-requirement-loop/blob/main/docs/handbook/index.md
- 协作仓库（提 Issue / Design·实现 PR）：https://github.com/quanttide-academy/quanttide-academy
- 产品代码仓库（跑程序）：https://github.com/hongwei-2026/product-requirement-loop
- 计分板：https://github.com/hongwei-2026/product-requirement-loop/blob/main/docs/%E4%BA%A4%E4%BB%98/%E4%BB%BB%E5%8A%A1%E8%AE%A1%E5%88%86%E6%9D%BF.md

### 人员信息

| **人名** | **GitHub ID** | **邮箱** | **角色** |
| :-- | :-- | :-- | :-- |
| 于鸿伟 | @hongwei-2026 | 待建 | 管理员 |
| 鲍宇航 | @Jerrybao99 | 待建 | 审核员 |
| 李可欣 | @likexin105 | 待建 | 审核员 |
| 黄亮 | @hl019 | 待建 | 审核员 |

### 总目标与步骤

目标：同事打开仓库只走一个入口，并能按写清的步骤完成一条需求梳理任务，交付物可按标准打勾。

1. 文档只留一个入口，目录命名向本仓库 `docs/specification/second-brain.md` 靠拢。
2. 每条要分配的任务写清目标、操作、验收和评审顺序，再进入分配。
3. 先做 [#6 顶栏 LLM 摘要](https://github.com/quanttide-academy/quanttide-academy/issues/6)，跑通后再拆后面的题。

### 工作流

> **协作地点：** 任务 Issue、Design PR、实现 PR 一律开在本仓库 `quanttide-academy/quanttide-academy`。产品代码在 `hongwei-2026/product-requirement-loop`，不要把交稿 PR 开到产品仓。

1. 在任务 Issue 里先写清要改仓库的哪一处。
2. 评论 `/claim`，系统把任务接到评论人。
3. 做完后提 PR。
4. 审核员在 PR 评论 `/通过`。人不必同时在线。
5. 管理员合并。

没有写清操作和验收的条目先保持提议中。

## 项目任务：文档入口归一

- Issue：[#5](https://github.com/quanttide-academy/quanttide-academy/issues/5)

- 优先级：紧急重要
- 所属项目：product-requirement-loop
- 文件位置：`hongwei-2026/product-requirement-loop` 的 `docs/handbook/index.md`；同事入口只放这一页
- 目标：不同技术背景的同事打开仓库，不需要在一堆中文文件名里找该看哪篇
- 任务要求：
	- [ ] 根 README 只指向 `docs/handbook/index.md`
	- [ ] 新文档放进 `docs/handbook`、`docs/specification` 或 `docs/tutorial`，文件名使用小写英文和连字符
	- [ ] `docs/交付`、`docs/阶段*` 保留为过程材料，从入口页标明「不是入口」
	- [ ] 入口页写明：Issue 沟通、`/claim` 接取、提 PR、审核员 `/通过`、管理员合并
- 参考资料：
	- [命名规范](docs/specification/second-brain.md)
	- [第二大脑改进建议](https://github.com/quanttide-academy/quanttide-academy/issues/1)
- 咨询对象：郭总
- 执行员：
	- [ ] 于鸿伟
- 评审员：王敏华
	- [ ] 王敏华
- 评审标准：
	- [ ] 任务要求全部满足
	- [ ] 打开根 README 只能看到一个同事入口
	- [ ] 措辞正式、准确、简洁、清晰
	- [ ] 评审员评审通过
- DDL：
	- 于鸿伟：26-10-08
	- 王敏华：26-10-10

## 项目任务：#1 顶栏展示模型摘要

- 优先级：紧急重要
- 所属项目：product-requirement-loop
- 文件位置：产品 Web 顶栏；任务说明见 [Issue #6](https://github.com/quanttide-academy/quanttide-academy/issues/6)
- 目标：登录后顶栏稳定显示当前 `provider`、`model`、`timeout`、`thinking_off`，排障时不用翻配置
- 任务要求：
	- [ ] 登录后顶栏能看到上述四项，刷新后仍在
	- [ ] 修改 `project/.env` 里的 provider 或 model 并重启后，顶栏跟着变
	- [ ] 页面和截图里不出现 API Key
	- [ ] `verify_lessons` 与 `verify_security` 仍通过
	- [ ] PR 正文写明改了哪个文件、怎么手动看到顶栏变化
- 参考资料：
	- [唯一入口](https://github.com/hongwei-2026/product-requirement-loop/blob/main/docs/handbook/index.md)
	- [Issue #6](https://github.com/quanttide-academy/quanttide-academy/issues/6)
- 咨询对象：于鸿伟
- 执行员：在 Issue #1 评论 `/claim` 后由系统接取
- 评审员：王敏华
	- [ ] 王敏华
- 评审标准：
	- [ ] 任务要求全部满足
	- [ ] 评审人按 PR 里的步骤能自己看到顶栏变化
	- [ ] 措辞与截图不包含密钥
	- [ ] 评审员评审通过后合并
- DDL：
	- 执行员：分配后 7 天
	- 王敏华：收到 PR 后 2 天

### 任务索引（未写清操作与验收前不分配）

| **难度** | **积分** | **任务** | **状态** |
| :-- | --: | :-- | :-- |
| 简单 | 10 | [#6 顶栏 LLM 摘要](https://github.com/quanttide-academy/quanttide-academy/issues/6) | 可领取 |
| 简单 | 15 | [#2 服务宕机 vs AI 超时](https://github.com/hongwei-2026/product-requirement-loop/issues/2) | 提议中 |
| 中等 | 30 | [#3 心跳与重试](https://github.com/hongwei-2026/product-requirement-loop/issues/3) | 提议中 |
| 中等 | 35 | [#4 待审库轻量搜索](https://github.com/hongwei-2026/product-requirement-loop/issues/4) | 提议中 |
| 难 | 60 | [#5 异步 Step1/2](https://github.com/hongwei-2026/product-requirement-loop/issues/5) | 提议中 |
| 难 | 50 | [#6 长日志压测 CI](https://github.com/hongwei-2026/product-requirement-loop/issues/6) | 提议中 |
| 难 | 55 | [#8 待审库工作台级分组](https://github.com/hongwei-2026/product-requirement-loop/issues/8) | 提议中 |
| 特难 | 75 | [#9 requirement.json 导出包](https://github.com/hongwei-2026/product-requirement-loop/issues/9) | 提议中 |
| 特难 | 80 | [#10 第二大脑 Context 导出包](https://github.com/hongwei-2026/product-requirement-loop/issues/10) | 提议中 |
| 特难 | 70 | [#11 SemVer 发布门禁](https://github.com/hongwei-2026/product-requirement-loop/issues/11) | 提议中 |
| 特难 | 75 | [#12 覆盖率 uncovered 面板](https://github.com/hongwei-2026/product-requirement-loop/issues/12) | 提议中 |
| 特难 | 70 | [#13 修订时间线 UI](https://github.com/hongwei-2026/product-requirement-loop/issues/13) | 提议中 |
| 特难 | 75 | [#14 打叉理由分析看板](https://github.com/hongwei-2026/product-requirement-loop/issues/14) | 提议中 |
| 特难 | 80 | [#15 待审库指派/SLA](https://github.com/hongwei-2026/product-requirement-loop/issues/15) | 提议中 |
| 特难 | 80 | [#16 Inbox 去重+冲突台](https://github.com/hongwei-2026/product-requirement-loop/issues/16) | 提议中 |
| 特难 | 85 | [#17 Step1 后入队 Step2 草稿](https://github.com/hongwei-2026/product-requirement-loop/issues/17) | 提议中 |
| 特难 | 85 | [#18 Prompt 版本 / prompt_sha](https://github.com/hongwei-2026/product-requirement-loop/issues/18) | 提议中 |
| 特难 | 90 | [#19 多 trial 矩阵](https://github.com/hongwei-2026/product-requirement-loop/issues/19) | 提议中 |
| 特难 | 90 | [#20 运行时切换 LLM](https://github.com/hongwei-2026/product-requirement-loop/issues/20) | 提议中 |
| 特难 | 75 | [#21 错误分类回流 lessons](https://github.com/hongwei-2026/product-requirement-loop/issues/21) | 提议中 |
| 特难 | 85 | [#22 JSON↔SQLite 单一数据源](https://github.com/hongwei-2026/product-requirement-loop/issues/22) | 提议中 |
