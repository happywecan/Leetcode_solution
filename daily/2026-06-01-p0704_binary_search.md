# 2026-06-01

## Problem

- Number: 704
- Title: Binary Search
- Link: https://leetcode.com/problems/binary-search/
- Difficulty: Easy
- Language: Java
- Attempt type: guided practice

## Initial Approach

Because the array is sorted, do not scan each element. Keep a left and right
boundary, check the middle, and remove half of the search range each time.

## Final Approach

1. Set `left = 0`.
2. Set `right = nums.length - 1`.
3. While `left <= right`, compute the middle index.
4. If `nums[middle] == target`, return `middle`.
5. If `nums[middle] < target`, move `left` to `middle + 1`.
6. Otherwise move `right` to `middle - 1`.
7. Return `-1` if the target is not found.

## Complexity

- Time: `O(log n)`
- Space: `O(1)`

## Mistakes and Review

- The problem asks for the index, not `true` or `false`.
- When searching the right half, use `left = middle + 1`, not `left = middle`.
- When searching the left half, use `right = middle - 1`.
- `middle = left + (right - left) / 2` avoids possible overflow.
