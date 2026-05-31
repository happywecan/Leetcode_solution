# 2026-05-31

## Problem

- Number: 217
- Title: Contains Duplicate
- Link: https://leetcode.com/problems/contains-duplicate/
- Difficulty: Easy
- Attempt type: reviewed with assistance

## Initial Approach

Compare values while iterating through the array. If a value has already
appeared, return `true`.

## Final Approach

Use a set to store values that have already been visited.

- Python: check `number in seen`, then call `seen.add(number)`.
- Java: call `seen.add(number)` directly. `HashSet.add()` returns `false` when
  the value already exists.

Return `false` after reaching the end without finding a duplicate.

## Complexity

- Time: `O(n)`
- Space: `O(n)`

## Mistakes and Review

- Review why set lookup is usually `O(1)`.
- Remember that Java uses `HashSet<Integer>` for integer values.
- Practice explaining the difference between Python `set` and Java `HashSet`.
