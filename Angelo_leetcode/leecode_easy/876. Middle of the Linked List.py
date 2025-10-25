# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        # 1. 初始化快慢指標，都指向頭節點
        slow = head
        fast = head
        
        # 2. 當快指標 (fast) 還沒到底，並且後面還有空間讓它走兩步時
        #    注意：fast 必須先走一步 (fast.next) 才能走第二步 (fast.next.next)
        while fast and fast.next:
            # 慢指標走一步
            slow = slow.next
            
            # 快指標走兩步
            fast = fast.next.next
            
        # 3. 循環結束時，慢指標 (slow) 正好在中間節點
        return slow



print(Solution.middleNode())
[1,2,3,4,5]