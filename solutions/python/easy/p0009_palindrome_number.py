"""LeetCode 9: Palindrome Number.

Problem: https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """Check whether an integer reads the same forwards and backwards.

        Time: O(log n)
        Space: O(1)
        """
        if x < 0:
            return False

        original = x
        reversed_number = 0
        while x:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10
        return original == reversed_number
