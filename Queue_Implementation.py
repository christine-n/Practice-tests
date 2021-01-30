"""
A queue is a first-in-first-out (FIFO) data structure. It can be implemented using a linked list.

The following are the three main operations that can be performed on a queue:

    enqueue: adding an element to the end of the list.

    dequeue: popping an item from the head of the list.

    peeking: displaying the element at the tail of the list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def enqueue(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def dequeue(self):
        temp = self.head
        if temp:
            element = temp.data
            self.head = temp.next
            return element
        else:
            # if head is None return None
            return temp

    # dispay an element from the tail of the linked list
    def peek(self):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            return current.data

    def printQueue(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.peek())
# print(queue.printQueue())
