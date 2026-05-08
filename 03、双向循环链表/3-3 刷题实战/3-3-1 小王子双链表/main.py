####################双向循环链表模板####################
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.dummy_head = Node(0)
        self.dummy_head.prev = self.dummy_head
        self.dummy_head.next = self.dummy_head
    
    def PushFront(self, value):
        new_node = Node(value)
        new_node.prev = self.dummy_head
        new_node.next = self.dummy_head.next
        self.dummy_head.next.prev = new_node
        self.dummy_head.next = new_node
        self.size += 1
    
    def PushBack(self, value):
        new_node = Node(value)
        new_node.prev = self.dummy_head.prev
        new_node.next = self.dummy_head
        self.dummy_head.prev.next = new_node
        self.dummy_head.prev = new_node
        self.size += 1
    
    def InsertAfter(self, node, value):
        if node is None or node == self.dummy_head:
            return
        new_node = Node(value)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        self.size += 1
    
    def DeleteNode(self, node):
        if node is None or node == self.dummy_head:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def Modify(self, node, value):
        if node is None:
            return
        node.data = value
    
    def Find(self, value):
        curr = self.dummy_head.next
        while curr != self.dummy_head:
            if curr.data == value:
                return curr
            curr = curr.next
        return None
    
    def Print(self):
        curr = self.dummy_head.next
        result = []
        while curr != self.dummy_head:
            result.append(str(curr.data))
            curr = curr.next
        print(' '.join(result))
    
    def Size(self):
        return self.size
    
    def Empty(self):
        return self.size == 0
####################双向循环链表模板####################

dll = DoublyLinkedList()

for i in range(1, 11):
    dll.PushBack(i)

n = int(input())
while n > 0:
    n -= 1
    x = int(input())
    nd = dll.Find(x)
    if nd is not None:
        nd.prev.next = nd.next
        nd.next.prev = nd.prev
        nd.prev = dll.dummy_head
        nd.next = dll.dummy_head.next
        dll.dummy_head.next.prev = nd
        dll.dummy_head.next = nd
    dll.Print()
