"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueTwoStacks:
    def __init__(self):
        self.front = None
        self.rear = None

        
    def enqueue(self, item):
        new_node = LinkedListNode(item)
        if self.rear is None:
            self.rear = new_node
            self.front = new_node
        #add new node to the rear
        #make sure the old rear points to the new node
        else:
            self.rear.next = new_node
        #take the rear point to new node
            self.rear = new_node


    def dequeue(self):
        if self.front is None:
            return None
        # store a temp variable so we dont lose our node
        old_front = self.front
        # move the front pointer, to the next node over
        self.front = self.front.next
        # Special case, if the queue should now be empty
        if self.front is None:
            self.rear = None
        return old_front.data

my_queue = QueueTwoStacks()

my_queue.enqueue("A")
my_queue.enqueue("B")
my_queue.enqueue("C")
my_queue.enqueue("D")

print(my_queue.front.data)
print(my_queue.rear.data)
print("Remove the value from the front")
print(f'removed value is {my_queue.dequeue()}')
print(f'removed value is {my_queue.dequeue()}')
print(f'The front is now {my_queue.front.data}')

print(my_queue.rear.data)