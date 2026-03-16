class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  

  
 
  
def find_kth_from_end(ll, k):
    # 1. 初始化快慢指標，都指向頭部
    slow = ll.head
    fast = ll.head
    
    # 2. 讓 fast 指標先走 k 步
    for _ in range(k):
        # 如果 k 大於串列長度，fast 會變成 None
        # 這時候代表沒辦法找到倒數第 k 個，回傳 None
        if fast is None:
            return None
        fast = fast.next
        
    # 3. 同時移動 slow 和 fast，直到 fast 走到盡頭
    while fast:
        slow = slow.next
        fast = fast.next
        
    # 4. 此時 slow 就是倒數第 k 個節點
    return slow



my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4



"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""

