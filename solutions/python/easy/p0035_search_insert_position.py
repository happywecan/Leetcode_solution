"""LeetCode 35: Search Insert Position.

Problem: https://leetcode.com/problems/search-insert-position/
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """Return the target index or the position where it should be inserted.

        Time: O(log n)
        Space: O(1)
        """
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle
        return left
