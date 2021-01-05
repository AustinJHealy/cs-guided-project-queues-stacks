
class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
       self.top = None

    def push(self, item):
        new_node = LinkedListNode(item)
        new_node.next = self.top
        # set the top variable to new node
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            old_top = self.top
            self.top = old_top.next

        old_top.next = None
        
        return old_top.data