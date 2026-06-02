# 2026-06-01

## Problem

- Number: 242
- Title: Valid Anagram
- Link: https://leetcode.com/problems/valid-anagram/
- Difficulty: Easy
- Language: Python
- Attempt type: guided practice

## Initial Approach

If the two strings have different lengths, they cannot be anagrams.
Otherwise, count every character in `s` with a dictionary, then use `t` to
subtract from those counts.

## Final Approach

1. Return `False` when the lengths are different.
2. Build a dictionary from characters in `s`.
3. Iterate through `t`.
4. If a character does not exist or its count is already `0`, return `False`.
5. Otherwise subtract `1`.
6. Return `True` after all characters are matched.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Mistakes and Review

- LeetCode must use `Python3` when the code has type hints such as `s: str`.
- Remember to remove unreachable placeholder code such as
  `raise NotImplementedError`.
- Dictionary counting is a core pattern for frequency problems.
