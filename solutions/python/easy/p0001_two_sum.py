"""LeetCode 1: Two Sum.

Problem: https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Return indices of two values that add up to target.

        Time: O(n)
        Space: O(n)
        """
        seen: dict[int, int] = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            seen[number] = index
        return []
