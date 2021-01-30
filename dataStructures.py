class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        self.items.pop(0)  # remove first item


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)

        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        if self.head:
            current = self.head
            myLL = ''
            while current:
                myLL += (str(current.val) + '->')
                print('{} -> '.format(current.val))
                current = current.next
            print(myLL)
        else:
            print('Empty')


"""
x=[1,2,3,4]
ll = LinkedList()
for i in x:
    ll.append(i)
ll.printLL()
"""


class QueueLL:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeque(self):
        if self.head is None:
            return None
        else:
            to_return = self.head
            self.head = self.head.next
            return to_return







