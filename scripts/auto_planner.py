#!/usr/bin/env python3
"""MaoXuan auto planner.

Input:
  - JSON via --input-json
  - or text todo list via --todo-text

Output:
  - Structured battle plan (JSON) with primary contradiction, attack tasks, time blocks,
    verification criteria, pivot conditions, and review prompts.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from typing import List, Dict


@dataclass
class Task:
    title: str
    estimate_min: int
    urgency: int
    impact: int
    uncertainty: int
    deps: List[str]


def detect_language(text: str, lang_flag: str) -> str:
    if lang_flag != "auto":
        return lang_flag
    zh = len(re.findall(r"[\u4e00-\u9fff]", text))
    en = len(re.findall(r"[A-Za-z]", text))
    # Prefer Chinese when user message has clear Chinese context.
    # This avoids accidental EN output when todos contain a few English tokens.
    if zh >= 6:
        return "zh"
    if zh > 0 and zh * 3 >= en:
        return "zh"
    return "en"


def parse_todo_text(text: str) -> List[Task]:
    tasks: List[Task] = []
    lines = [ln.strip("-• \t") for ln in text.splitlines() if ln.strip()]
    for ln in lines:
        # Optional pattern: "task | est=45 | urgency=4 | impact=5 | uncertainty=3 | deps=a,b"
        parts = [p.strip() for p in ln.split("|")]
        title = parts[0]
        meta: Dict[str, str] = {}
        for p in parts[1:]:
            if "=" in p:
                k, v = p.split("=", 1)
                meta[k.strip().lower()] = v.strip()
        task = Task(
            title=title,
            estimate_min=int(meta.get("est", 45)),
            urgency=int(meta.get("urgency", 3)),
            impact=int(meta.get("impact", 3)),
            uncertainty=int(meta.get("uncertainty", 3)),
            deps=[d.strip() for d in meta.get("deps", "").split(",") if d.strip()],
        )
        tasks.append(task)
    return tasks


def parse_json_input(payload: str) -> Dict:
    data = json.loads(payload)
    if "tasks" not in data:
        raise ValueError("JSON input must contain `tasks`.")
    return data


def score_task(t: Task) -> float:
    # Higher urgency + impact => higher priority; uncertainty and long duration reduce attackability.
    return t.urgency * 1.2 + t.impact * 1.8 - t.uncertainty * 0.8 - (t.estimate_min / 120)


def build_plan(goal: str, tasks: List[Task], lang: str, work_block_min: int) -> Dict:
    if not tasks:
        raise ValueError("No tasks parsed. Provide at least one todo item.")

    ranked = sorted(tasks, key=score_task, reverse=True)
    primary = ranked[0]
    secondary = ranked[1:4]

    immediate = ranked[: min(3, len(ranked))]
    blocks = []
    for i, t in enumerate(immediate, 1):
        dur = min(max(25, t.estimate_min), work_block_min)
        blocks.append({"block": i, "duration_min": dur, "task": t.title, "done_if": f"完成可见产物: {t.title}" if lang == "zh" else f"Visible artifact done: {t.title}"})

    if lang == "zh":
        return {
            "战略目标": goal,
            "当前主要矛盾": primary.title,
            "主要矛盾判定依据": "综合影响度、紧急度、可攻击性评分最高。",
            "次要矛盾": [t.title for t in secondary],
            "当前战役目标": f"优先突破主要矛盾：{primary.title}",
            "本轮突击任务": [t.title for t in immediate],
            "时间块安排": blocks,
            "验证标准": [
                "每个时间块产出一个可见成果（文档/代码/日志/表格）。",
                "本轮结束能判断推进/僵持。",
            ],
            "转移阵地条件": [
                "同一阻塞在两种路径重复出现。",
                "单任务投入超过预估2倍仍无可见进展。",
            ],
            "复盘问题": [
                "今天是否命中主要矛盾？",
                "最大阻塞的证据是什么？",
                "下轮15-30分钟可开工动作是什么？",
            ],
            "任务评分": [{"title": t.title, "score": round(score_task(t), 2)} for t in ranked],
        }

    return {
        "Strategic Goal": goal,
        "Primary Contradiction": primary.title,
        "Why Primary": "Highest combined score from impact, urgency, and attackability.",
        "Secondary Contradictions": [t.title for t in secondary],
        "Current Campaign Objective": f"Break the primary bottleneck first: {primary.title}",
        "Immediate Attack Tasks": [t.title for t in immediate],
        "Time Blocks": blocks,
        "Verification": [
            "Each block must produce one visible artifact (doc/code/log/table).",
            "At round end, classify result as advance/partial/stalemate.",
        ],
        "Pivot Conditions": [
            "Same blocker appears in two different routes.",
            "Time spent exceeds 2x estimate with no visible progress.",
        ],
        "Review Questions": [
            "Did we hit the primary contradiction today?",
            "What is the strongest evidence for the current blocker?",
            "What is the next 15-30 minute opening move?",
        ],
        "Task Scores": [{"title": t.title, "score": round(score_task(t), 2)} for t in ranked],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Auto planner for MaoXuan research ops")
    parser.add_argument("--goal", required=True, help="Strategic goal / 战略目标")
    parser.add_argument("--todo-text", help="Multiline todo text")
    parser.add_argument("--input-json", help="JSON payload with tasks")
    parser.add_argument("--lang", choices=["auto", "zh", "en"], default="auto")
    parser.add_argument("--work-block-min", type=int, default=90)
    args = parser.parse_args()

    if not args.todo_text and not args.input_json:
        raise SystemExit("Provide --todo-text or --input-json")

    if args.input_json:
        data = parse_json_input(args.input_json)
        tasks = [
            Task(
                title=t["title"],
                estimate_min=int(t.get("estimate_min", 45)),
                urgency=int(t.get("urgency", 3)),
                impact=int(t.get("impact", 3)),
                uncertainty=int(t.get("uncertainty", 3)),
                deps=list(t.get("deps", [])),
            )
            for t in data["tasks"]
        ]
        sample_text = args.goal + "\n" + "\n".join(t.title for t in tasks)
    else:
        tasks = parse_todo_text(args.todo_text)
        sample_text = args.goal + "\n" + args.todo_text

    lang = detect_language(sample_text, args.lang)
    plan = build_plan(args.goal, tasks, lang, args.work_block_min)
    print(json.dumps(plan, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
