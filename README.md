# MaoXuan Research Ops Skill

This repository contains a MaoXuan-style research execution skill and an automatic planner script.

## Structure

- `SKILL.md`: Core skill definition (single-language body + language switching rule)
- `templates/battle-plan-template.md`: Reusable execution template
- `examples/diffusion-vlm-integration.md`: Applied example
- `scripts/auto_planner.py`: Auto planner that turns todos into a structured battle plan

## Auto planner quick start

### Text todos

```bash
python scripts/auto_planner.py \
  --goal "完成扩散VLM对比实验并产出可复现结果" \
  --todo-text $'跑baseline | est=50 | urgency=5 | impact=5 | uncertainty=2\n复现报错并定位 | est=40 | urgency=4 | impact=5 | uncertainty=3\n整理实验表格 | est=30 | urgency=3 | impact=3 | uncertainty=1' \
  --lang auto
```

### JSON todos

```bash
python scripts/auto_planner.py \
  --goal "Build a reproducible benchmark pipeline" \
  --input-json '{"tasks":[{"title":"run baseline","urgency":5,"impact":5,"uncertainty":2},{"title":"integrate method A","urgency":4,"impact":4,"uncertainty":3}]}' \
  --lang en
```
