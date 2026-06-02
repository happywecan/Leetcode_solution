
"""LeetCode 242: Valid Anagram.

Problem: https://leetcode.com/problems/valid-anagram/
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Return whether t is an anagram of s.

        Time: O(n)
        Space: O(n)
        """
        if len(s) != len(t):
            return False

        count = {}

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))  # Expected: True
    print(solution.isAnagram("rat", "car"))          # Expected: False
