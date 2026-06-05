# 2026-06-04

## Problem

- Number: 35
- Title: Search Insert Position
- Link: https://leetcode.com/problems/search-insert-position/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## Initial Approach

The array is sorted, so use binary search instead of scanning each number.
The twist is that when the target is missing, the answer is the index where the
target should be inserted.

## Final Approach

1. Set `left = 0`.
2. Set `right = nums.length` so the search range is `[left, right)`.
3. While `left < right`, compute the middle index.
4. If `nums[middle] < target`, the target must be after `middle`, so set
   `left = middle + 1`.
5. Otherwise, `middle` could be the answer, so set `right = middle`.
6. When the loop ends, return `left`.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Mistakes and Review

- This problem returns an insertion index, not `-1` when the target is missing.
- With the `[left, right)` style, start with `right = nums.length`.
- Use `right = middle`, not `right = middle - 1`, because `middle` may be the
  first valid insert position.
