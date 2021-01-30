# Definition for singly-linked list.
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode

    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

    def countNodes(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        print(counter)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_ll = LinkedList()
        l2_ll = LinkedList()
        # print(l1[::-1])
        for i in l1:
            l1_ll.push(i)
        for i in l2:
            l2_ll.push(i)
        # print(l1_ll, l2_ll)
        res = LinkedList()
        # l1_ll.printLL()
        # l2_ll.printLL()
        res.adding(l1_ll.head, l2_ll.head)
        res.printLL()
        # l2_ll.countNodes()

    def adding(self, l1, l2):
        prev = None
        temp = None
        carry = 0

        while l1 is not None or l2 is not None:
            l1_data = 0 if l1 is None else l1.data
            l2_data = 0 if l2 is None else l2.data
            _sum = carry + l1_data + l2_data

            # update carry for next calculation
            carry = 1 if _sum >= 10 else 0

            # update _sum if it is greater than 10
            _sum = _sum if _sum < 10 else _sum % 10

            temp = ListNode(_sum)
            # if this is the first node then set it as head
            # of resultant list
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            # Set prev for next insertion
            prev = temp

            # Move first and second pointers to next nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        if carry > 0:
            temp.next = ListNode(carry)


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        l3 = None
        temp = None
        carry = 0

        while l1 is not None or l2 is not None:
            l1_data = 0 if l1 is None else l1.val
            l2_data = 0 if l2 is None else l2.val

            _sum = carry + l1_data + l2_data

            _sum = _sum if _sum < 10 else _sum % 10
            carry = 0 if _sum < 10 else 1

            l1 = l1.next
            l2 = l2.next

            temp = Node(_sum)

            if l3 is None:
                l3 = temp
            else:
                l3.next = temp
                l3 = l3.next
                print(l3)

        if carry > 0:
            temp = Node(_sum)
            l3.next = temp
            l3 = l3.next

        return l3


if __name__ == '__main__':
#     l1 = [2, 4, 3]
#     l2 = [5, 6, 4]
    l1 = Node{val: 2, next: Node{val: 4, next: Node{val: 3, next: None}}}
    l2 = Node{val: 5, next: Node{val: 6, next: Node{val: 4, next: None}}}
    s = Solution()
    s.addTwoNumbers(l1, l2)
