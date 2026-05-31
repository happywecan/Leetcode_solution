#!/usr/bin/env python3
import argparse
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a LeetCode solution template and daily note.")
    parser.add_argument("number", type=int, help="LeetCode problem number")
    parser.add_argument("slug", help="Problem slug, for example: two-sum")
    parser.add_argument("difficulty", choices=("easy", "medium", "hard"))
    parser.add_argument("--date", default=date.today().isoformat(), help="Practice date in YYYY-MM-DD format")
    return parser.parse_args()


def create_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise SystemExit(f"Refusing to overwrite existing file: {path.relative_to(ROOT)}")
    path.write_text(content, encoding="utf-8")
    print(f"Created {path.relative_to(ROOT)}")


def main() -> None:
    args = parse_args()
    module_name = f"p{args.number:04d}_{args.slug.replace('-', '_')}"
    solution_path = ROOT / "solutions" / "python" / args.difficulty / f"{module_name}.py"
    daily_path = ROOT / "daily" / f"{args.date}-{module_name}.md"
    problem_url = f"https://leetcode.com/problems/{args.slug}/"

    solution = f'''"""LeetCode {args.number}: {args.slug.replace("-", " ").title()}.

Problem: {problem_url}
"""


class Solution:
    pass
'''

    daily_note = f"""# {args.date}

## Problem

- Number: {args.number}
- Title: {args.slug.replace("-", " ").title()}
- Link: {problem_url}
- Difficulty: {args.difficulty.title()}
- Attempt type: independent / hint-assisted / reviewed with assistance

## Initial Approach

Write the first idea before checking references.

## Final Approach

Explain the algorithm in your own words.

## Complexity

- Time:
- Space:

## Mistakes and Review

- What was confusing?
- What should be reviewed tomorrow?
"""

    create_file(solution_path, solution)
    create_file(daily_path, daily_note)


if __name__ == "__main__":
    main()
