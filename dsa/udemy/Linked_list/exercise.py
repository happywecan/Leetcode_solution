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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
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

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        # 1. 交換 head 和 tail 的位置
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        # 2. 初始化三個指針
        # before: 當前節點的前一個 (一開始是 None，因為原本的 head 反轉後變最後一個)
        # after: 當前節點的下一個 (用來暫存，避免斷掉連結後找不到路)
        before = None
        
        # 3. 開始遍歷並反轉
        for _ in range(self.length):
            # 先存下原本的下一個節點
            after = temp.next
            
            # 關鍵動作：將當前節點的 next 指向前一個節點 (反轉箭頭)
            temp.next = before
            
            # 指針向後移動一位，準備處理下一個節點
            before = temp
            temp = after




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print('LL before reverse():')
my_linked_list.print_list()

my_linked_list.reverse()

print('\nLL after reverse():')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    LL before reverse():
    1
    2
    3
    4

    LL after reverse():
    4
    3
    2
    1
    
"""