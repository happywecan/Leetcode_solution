# LeetCode Practice Log

Daily data-structure and algorithm practice in Python.

This repository is a public learning log. It records reviewed solutions,
implementation notes, and older drafts so progress remains visible over time.
The goal is consistent practice and clear reasoning, not a claim that every
solution was written without references or tooling assistance.

## Repository Structure

```text
solutions/python/       Reviewed LeetCode solutions
tests/                  Regression tests for reviewed solutions
daily/                  Daily practice notes
dsa/udemy/              Data-structure course exercises
archive/legacy/          Early drafts and incomplete learning attempts
scripts/new_problem.py   Creates a daily note and solution template
```

## Reviewed Solutions

| # | Problem | Difficulty | Solution |
| ---: | --- | --- | --- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [Python](solutions/python/easy/p0001_two_sum.py) |
| 9 | [Palindrome Number](https://leetcode.com/problems/palindrome-number/) | Easy | [Python](solutions/python/easy/p0009_palindrome_number.py) |
| 13 | [Roman to Integer](https://leetcode.com/problems/roman-to-integer/) | Easy | [Python](solutions/python/easy/p0013_roman_to_integer.py) |
| 14 | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) | Easy | [Python](solutions/python/easy/p0014_longest_common_prefix.py) |
| 20 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | [Python](solutions/python/easy/p0020_valid_parentheses.py) |
| 35 | [Search Insert Position](https://leetcode.com/problems/search-insert-position/) | Easy | [Python](solutions/python/easy/p0035_search_insert_position.py) |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | [Python](solutions/python/easy/p0121_best_time_to_buy_and_sell_stock.py) |
| 136 | [Single Number](https://leetcode.com/problems/single-number/) | Easy | [Python](solutions/python/easy/p0136_single_number.py) |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | [Python](solutions/python/easy/p0283_move_zeroes.py) |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | Easy | [Python](solutions/python/easy/p0344_reverse_string.py) |
| 876 | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) | Easy | [Python](solutions/python/easy/p0876_middle_of_the_linked_list.py) |

## Daily Workflow

Create a template for the day's problem:

```bash
python3 scripts/new_problem.py 3 longest-substring-without-repeating-characters medium
```

Then:

1. Write down the initial approach before looking up a solution.
2. Implement or review the algorithm.
3. Record complexity and mistakes in `daily/YYYY-MM-DD.md`.
4. Add tests when promoting a solution into `solutions/python/`.
5. Commit the daily progress.

```bash
python3 -m unittest discover -s tests -v
git add .
git commit -m "Practice: <problem name>"
git push origin main
```

## Assistance Policy

References, discussions, and AI tools may be used for review. Daily notes
should state whether a solution was solved independently, completed after a
hint, or reviewed with assistance. The useful signal is the reasoning,
correction process, and ability to explain the final implementation.

## Archive

The archive intentionally retains early drafts and incomplete attempts. They
are not presented as reviewed solutions. This keeps the main solution index
clean while preserving the learning history.
