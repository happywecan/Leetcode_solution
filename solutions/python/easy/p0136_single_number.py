"""LeetCode 136: Single Number.

Problem: https://leetcode.com/problems/single-number/
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Use XOR because equal values cancel each other out.

        Time: O(n)
        Space: O(1)
        """
        result = 0
        for number in nums:
            result ^= number
        return result
