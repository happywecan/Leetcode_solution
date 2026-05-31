"""LeetCode 20: Valid Parentheses.

Problem: https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """Validate closing brackets against the most recent opening bracket.

        Time: O(n)
        Space: O(n)
        """
        pairs = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []
        for character in s:
            if character in pairs.values():
                stack.append(character)
            elif not stack or stack.pop() != pairs[character]:
                return False
        return not stack
