# A linked list node
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

    dummy = Node()	  # Dummy node is temporarily the first node
    tail = dummy		# Start the tail at the dummy.

    # Build the list on dummy.next (aka tail.next)
    for key in keys:
        tail.next = push(tail.next, key)
        tail = tail.next

    # The real result list is now in dummy.next
    # dummy.next == key[0], key[1], key[2], key[3]
    return dummy.next


if __name__ == '__main__':

    # input keys
    keys = [1, 2, 3, 4]

    # points to the head node of the linked list
    head = constructList(keys)

    # print linked list
    printList(head)
