"""LeetCode 283: Move Zeroes.

Problem: https://leetcode.com/problems/move-zeroes/
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Move non-zero values forward, then fill the remaining slots.

        Time: O(n)
        Space: O(1)
        """
        write_index = 0
        for number in nums:
            if number != 0:
                nums[write_index] = number
                write_index += 1
        for index in range(write_index, len(nums)):
            nums[index] = 0
