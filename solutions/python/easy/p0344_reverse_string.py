"""LeetCode 344: Reverse String.

Problem: https://leetcode.com/problems/reverse-string/
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Swap characters from both ends until the pointers meet.

        Time: O(n)
        Space: O(1)
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
