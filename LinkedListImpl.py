# A single node of a singly linked list
class Node:
    # Constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to print given linked list
def printList(head):
    ptr = head
    while ptr:
        print(ptr.data, end=" -> ")
        ptr = ptr.next


# Takes a list and a data value and creates a link with given data
# and pushes it onto the front of the list.
def push(head, data):

    # Allocate the node in the heap and set its data
    newNode = Node(data)

    # Set the next field of the node to point to the current
    # first node of the list.
    newNode.next = head

    # Change the head to point to the node, so it is
    # now the first node in the list.
    print(newNode.next)
    return newNode


# Function to implement linked list from given set of keys
# using dummy node
def constructList(keys):

    dummy = Node()    # Dummy node is temporarily the first node
    tail = dummy        # Start the tail at the dummy.

    # Build the list on dummy.next (aka tail.next)
    for key in keys:
        tail.next = push(tail.next, key)
        tail = tail.next

    # The real result list is now in dummy.next
    # dummy.next == key[0], key[1], key[2], key[3]
    return dummy.next


# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            print(current.data, end=" -> ")
            current = current.next
        print('\n')

    # insertion method for the linked list
    def append(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def prepend(self, data):
        newNode = Node(data)
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insert_after_node(self, data, node):
        newNode = Node(data)
        if self.head:
            current = self.head
            while current:
                if current.data == node:
                    newNode.next = current.next
                    current.next = newNode
                current = current.next

    def reverse(self):
        if self.head:
            current = self.head
            prev = None
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node

            self.head = prev


if __name__ == '__main__':

    #     # input keys
    # keys = [1, 2, 3, 4]

    # # points to the head node of the linked list
    # head = constructList(keys)

    # # print linked list
    # printList(head)


    # Singly Linked List with insertion and print methods
    LL = LinkedList()
    LL.append(3)
    LL.append(4)
    LL.append(5)
    LL.prepend(2)
    LL.insert_after_node(10, 4)
    LL.reverse()
    LL.printLL()
