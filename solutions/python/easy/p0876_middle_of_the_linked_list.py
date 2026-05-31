"""LeetCode 876: Middle of the Linked List.

Problem: https://leetcode.com/problems/middle-of-the-linked-list/
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Advance one pointer once and another pointer twice per loop.

        Time: O(n)
        Space: O(1)
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
