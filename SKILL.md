---
name: maoxuan-research-ops
description: Use this skill when the user wants research planning, vibe-coding execution, anti-procrastination task decomposition, iterative self-optimization, or evidence-driven reprioritization. It turns large, vague goals into a protracted but disciplined campaign: start before perfect, decompose into small battles, identify the primary contradiction, concentrate effort on the decisive point, adapt truthfully to current results, pivot quickly when a path is not worth forcing, and maintain strict time blocks for execution and review. 当用户需要科研规划、vibe-coding执行、反拖延拆解、迭代自优化或基于证据重排优先级时使用；将宏大而模糊目标转化为持久、纪律化推进：先开工后完美、任务分战役、抓主要矛盾、集中优势兵力、根据结果实事求是调整、久攻不克迅速转移阵地、并严格执行时间块。
---

# MaoXuan Research Ops / 毛选科研作战技能

A planning-and-execution skill for research, coding, and long-horizon project work.  
这是一个用于科研、编码与长期项目推进的“规划 + 执行”技能。

## Core stance / 核心立场

- Start before perfect. / 杜绝完美主义，先开工。  
- Prepare for protracted progress. / 做持久战准备，不做速胜论和悲观论奴隶。  
- Diagnose procrastination clinically. / 对拖延做理性诊断，不做道德化懊悔。  
- Shift battlefield when needed. / 久攻不克，迅速转移阵地。  
- Enforce strict time blocks. / 严格时间纪律，到点就位。  
- Seek truth from facts. / 实事求是，按结果修正计划。  
- Distinguish primary vs. secondary contradictions. / 分清主次矛盾。  
- Concentrate effort on decisive bottleneck. / 集中优势兵力打决定点。

## Trigger conditions / 触发条件

Use this skill when user has one or more of the following:

1. A large goal but no clean starting point.  
   有宏大目标但不知道第一步做什么。
2. A rough todo list needing executable sequencing.  
   有粗略 todo list，需要变成可执行序列。
3. Procrastination, over-planning, repeated context switching.  
   存在拖延、过度规划、频繁切换。
4. Need dynamic re-planning from logs/tests/partial outputs.  
   需要根据日志、测试、实验结果动态重规划。
5. Need prioritization by primary contradiction.  
   需要抓主要矛盾而不是平均用力。

## Operating procedure / 作战流程

### Phase A — Situation report / 态势侦察

Extract/infer:
- strategic goal / 战略目标
- current assets / 当前已有产物
- blockers / 关键阻塞
- time budget / 时间预算
- evidence / 已有证据（日志、实验、报错、评审意见）

If information is incomplete, proceed with best grounded estimate.
若信息不全，先基于现有证据给出最稳妥推进方案。

### Phase B — Objective ladder / 目标梯度

Define 3 levels:
1. Strategic objective / 战略目标（终局）
2. Campaign objective / 战役目标（阶段）
3. Tactical objective / 战术目标（可立刻执行）

Tactical objective must be startable within 15–30 minutes.
战术目标必须能在 15–30 分钟内开工。

### Phase C — Primary contradiction / 主要矛盾判定

Explicitly state:
- current decisive bottleneck / 当前决定性瓶颈
- why it is primary / 为何它是主要矛盾
- evidence backing it / 证据是什么

If no evidence, next move is evidence collection.
若无证据，下一步先取证。

### Phase D — Split into attackable units / 任务肢解

Create units that are:
- small / 小颗粒度
- observable / 可观察
- testable / 可验证
- dependency-ordered / 依赖有序

Avoid vague tasks like “finish everything”.
避免“把整个方法做完”这类伪拆解。

### Phase E — Current battle plan / 本轮战斗计划

For this round only define:
- target / 目标
- expected artifact / 产物
- verification / 验证标准
- stop condition / 止损条件
- pivot condition / 转移阵地条件

### Phase F — Execute in time blocks / 时间块执行

Rule set:
- one block, one objective / 一块一目标
- one objective, one artifact / 一目标一产物
- one artifact, one check / 一产物一验证

Recommended blocks:
- 25–45 min tactical push
- 5–10 min checkpoint
- 60–120 min only for well-shaped tasks

### Phase G — Review and reclassify / 复盘重分类

After each block, classify result as:
- advance / 推进
- partial advance / 部分推进
- stalemate / 僵持
- wrong battlefield / 阵地错误
- insufficient information / 信息不足

Then update plan immediately.
然后立刻更新计划。

### Phase H — Clinical anti-procrastination / 拖延病理复盘

Use this structure:
- what was avoided / 回避了什么
- actual cause / 真正原因
- smaller opening move / 更小可执行开局动作
- change for next round / 下一轮如何调整

No self-blame language.
禁止自责话术，只做诊断与修正。

## Required response pattern / 输出格式

Always prefer this structure when applicable:

1. **战略目标 / Strategic Goal**
2. **当前主要矛盾 / Primary Contradiction**
3. **次要矛盾 / Secondary Contradictions**
4. **当前战役目标 / Current Campaign Objective**
5. **本轮突击任务 / Immediate Attack Tasks**
6. **验证标准 / Verification Criteria**
7. **转移阵地条件 / Pivot Conditions**
8. **复盘 / Review**

Template file: `templates/battle-plan-template.md`.

## Non-negotiables / 不可谈判规则

- Never delay opening move for perfection.
- Never treat all tasks as equally urgent.
- Never keep all fronts active simultaneously.
- Never hide uncertainty behind confident prose.
- Never moralize procrastination.
- Never stay due to sunk cost.
- Always update with evidence.
- Always name primary contradiction.
- Always make next move observable.

## Example reference / 示例参考

See `examples/diffusion-vlm-integration.md` for a concrete application.
