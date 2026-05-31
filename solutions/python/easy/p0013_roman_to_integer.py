"""LeetCode 13: Roman to Integer.

Problem: https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        """Convert a Roman numeral by subtracting values before larger values.

        Time: O(n)
        Space: O(1)
        """
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for index, character in enumerate(s):
            value = values[character]
            if index + 1 < len(s) and value < values[s[index + 1]]:
                total -= value
            else:
                total += value
        return total
