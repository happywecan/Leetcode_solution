"""LeetCode 217: Contains Duplicate.

Problem: https://leetcode.com/problems/contains-duplicate/
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return whether any value appears more than once.

        Time: O(n)
        Space: O(n)
        """
        seen: set[int] = set()
        for number in nums:
            if number in seen:
                return True
            seen.add(number)
        return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1, 2, 3, 1]))
    print(solution.containsDuplicate([1, 2, 3, 4]))
