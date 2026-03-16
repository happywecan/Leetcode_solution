class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def has_loop(self):
        # 1. 初始化快慢指標
        slow = self.head
        fast = self.head

        # 2. 當快指標還能往後走兩步時繼續執行
        while fast is not None and fast.next is not None:
            # 慢指標走一步，快指標走兩步
            slow = slow.next
            fast = fast.next.next
            
            # 3. 如果在移動後，快慢指標指到同一個節點，代表有環
            if slow == fast:
                return True
        
        # 4. 如果快指標走到了終點（None），代表沒有環
        return False
    
    
my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() ) # Returns True




my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop() ) # Returns False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
