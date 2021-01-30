"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

Write a function:
that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
For example, given
    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8].
A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]
"""


def cyclicRotation(K, A):
    # x = [3, 8, 9, 7, 6] # -> [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    # [3, 8, 9, 7, 6] , 3  -> [9, 7, 6, 3, 8]
    # [1, 1, 2, 3, 5], 42 -> [3, 5, 1, 1, 2]
    if len(A) == 0:
        return A
    K = K % len(A)
    if K == 0:
        return A

    return (A[-K:] + A[:len(A) - K])


"""
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
{ i : A ≤ i ≤ B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
Write an efficient algorithm for the following assumptions:
11, 345, 17 => 20
"""


def countDiv(A, B, K):
    counter = 0
    for i in range(A, B + 1):
        print(i)
        if i % K == 0:
            counter += 1
    return (counter)
# countDiv(6, 11, 2) # 3


def countDiv(A, B, K):
    return (B // K - A // K) + (1 if A % K == 0 and A > K else 0)

# countDiv(11, 345, 17) # 20


def charOccurrenceinWord(s):
    occurrences = [0] * 26
    n = len(s)

    for i in range(n):
        occurrences[ord(s[i]) - ord('a')] += 1

    highest_occ = max(occurrences)
    letter = 'a'
    for i in range(1, len(occurrences)):
        if occurrences[i] >= highest_occ:
            letter = chr(ord('a') + i)
            highest_occ = occurrences[i]
    return letter


def wordMachine(s):
    # 4 5 6 - 7 +
    # 3 DUP 5 - -
    # 5 6 + -
    if len(s) == 0:
        return -1
    s = s.split(' ')
    # actions: push DUP POP + -
    stack = []
    print(s)
    for val in s:
        try:
            if val == 'DUP':
                cur = stack.pop()
                stack.append(cur)
                stack.append(cur)
            elif val == 'POP':
                cur = stack.pop()
            elif val == '+':
                cur1 = stack.pop()
                cur2 = stack.pop()
                stack.append(cur1 + cur2)
            elif val == '-':
                cur1 = stack.pop()
                cur2 = stack.pop()
                stack.append(cur1 - cur2)
            else:
                stack.append(int(val))
        except:
            return -1

    return stack[-1]
# print(wordMachine(''))


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    minStrs, maxStrs, i = min(strs), max(strs), 0
    for i in range(min(len(minStrs), len(maxStrs))):
        if minStrs[i] != maxStrs[i]:
            break
        else:
            i += 1
    return minStrs[:i]

# print(longestCommonPrefix(["flower","flow","flight"]))


def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    """
    # can we sort?
    # can nums be empty
    # can nums be less than 3

    nums.sort()
    [-4, -1, -1, 0, 1 ,2] => [[-1,-1,2],[-1,0,1]]
    target = 0

    [3,-2,-1]
    [3,-2,1,0] => []
    [3,0,-2,-1,1,2] => [[-2,-1,3],[-2,0,2],[-1,0,1]]

    """
    uRes = set()
    n = len(nums)
    target = 0
    res = []

    if n < 3:
        return []
    nums.sort()
    print(nums)  # [-2, -1, 0, 1, 2, 3]
    for i in range(n):
        left = i + 1
        right = n - 1
        while left <= right:
            print(nums[i], nums[left], nums[right])
            calcSum = nums[i] + nums[left] + nums[right]
            if calcSum < target:
                right -= 1
            elif calcSum > target:
                left += 1
            else:
                if (nums[i], nums[left], nums[right]) not in uRes:
                    res.append([nums[i], nums[left], nums[right]])
                uRes.add((nums[i], nums[left], nums[right]))
                # right -= 1
                left += 1

    return res

# print(threeSum([3,0,-2,-1,1,2]))


def isValid(s):
    """
    :type s: str
    :rtype: bool
    (){}}{

    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in mapping:
            top = stack.pop() if stack else ' '

            if mapping[i] != top:
                return False
        else:
            stack.append(i)

    return not stack
# print(isValid("["))


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, val):
        newNode = ListNode(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printll(self):
        if self.head:
            current = self.head
            while current:
                print(current.val)
                current = current.next
        else:
            print('Empty')


class Solution():
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode()

        while l1 and l2:
            if l1.val < l2.val:
                l3.val = l1.val
                l1.val = l1.next
            elif l1.val > l2.val:
                l3.val = l2.val
                l2.val = l2.next


# s = Solution()
# a1 = [1, 2, 4]
# a2 = [1, 3, 4]
# l1 = LinkedList()
# l2 = LinkedList()

# for i in a1:
#     l1.add(i)

# for i in a2:
#     l2.add(i)


# l1.printll()
# l2.printll()
# s.mergeTwoLists(l1, l2)

def mergeSortedArrays(nums1, m, nums2, n):
    """
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    nums1=[1], m=1, nums2=[], n=0
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    # Start from the end index of nums1 and walk back inserting the largest number every time:
    for i in range(m + n - 1, -1, -1):
        if m and (not n or nums1[m - 1] > nums2[n - 1]):
            nums1[i] = nums1[m - 1]
            m -= 1
        else:
            nums1[i] = nums2[n - 1]
            n -= 1
    print(nums1)
# mergeSortedArrays(nums1 = [1,2,3,5,0,0,0], m = 4, nums2 = [2,5,6], n = 3)


def fibonnacciRec(n, cache):
    """
    0 = 1
    1 = 1
    2 = 1 + 1 = 2
    3 = 2 + 1 = 3
    4 = 3 + 2 = 5
    5 = (n-1)+ (n - 2) = 8
    """
    if n in cache:
        return cache[n]
    if n < 3:
        return 1
    fib = fibonnacciRec(n - 1, cache) + fibonnacciRec(n - 2, cache)
    cache[n] = fib
    return fib


def fibonnacci(n):
    """
    0 = 1
    1 = 1
    2 = 1 + 1 = 2
    3 = 2 + 1 = 3
    4 = 3 + 2 = 5
    5 = (n-1)+ (n - 2) = 8
    """
    if n < 2:
        return 1
    fib = [1, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

"""
Given a string of integers of len btn 4 and 12. Get all combinations of ip addresses available
"""
def isValid(s):
    intS = int(s)
    if intS > 255:
        return False
    return len(str(intS)) == len(s) # check for leading 0


def ipAddress(s):
    n = len(s)
    ips = []
    for i in range(1, min(n, 4)):
        currentIP = ['', '', '', '']
        currentIP[0] = s[:i]
        if not isValid(currentIP[0]):
            continue
        for j in range(i + 1, i + min(n - i, 4)):
            currentIP[1] = s[i:j]
            if not isValid(currentIP[0]):
                continue
            for k in range(j + 1, j + min(n - j, 4)):
                currentIP[2] = s[j:k]
                currentIP[3] = s[k:]
                if isValid(currentIP[2]) and isValid(currentIP[3]):
                    ips.append('.'.join(currentIP))

    return ips


print(ipAddress('123405'))
