"""LeetCode 14: Longest Common Prefix.

Problem: https://leetcode.com/problems/longest-common-prefix/
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Shrink the candidate prefix until every word starts with it.

        Time: O(n * m)
        Space: O(1)
        """
        if not strs:
            return ""

        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
