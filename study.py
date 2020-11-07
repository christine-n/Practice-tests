def minimumSwap():
    """
    You are given an unordered array consisting of consecutive integers
    [1, 2, 3, ..., n] without any duplicates. You are allowed to swap
    any two elements. You need to find the minimum number of swaps
    required to sort the array in ascending order.

    For example, given the array arr=[7, 1, 3, 2, 4, 5, 6] we
    perform the following steps:
    i   arr                     swap (indices)
    0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
    1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
    2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
    3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
    4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
    5   [1, 2, 3, 4, 5, 6, 7]
    It took 5 swaps to sort the array.

    Function Description

    Complete the function minimumSwaps in the editor below.
    It must return an integer representing the minimum number of
     swaps to sort the array.
    minimumSwaps has the following parameter(s):

    arr: an unordered array of integers
    Given array arr [1, 3, 5, 2, 4, 6, 7]
    After swapping (1,3) we get [1, 2, 5, 3, 4, 6, 7]
    After swapping (2,3) we get [1, 2, 3, 5, 4, 6, 7]
    After swapping (3,4) we get [1, 2, 3, 4, 5, 6, 7]
    """
    arr = [2, 1, 3, 7, 4, 5, 6]
    n = len(arr)
    counter = 0
    for i in range(n):
        already_sorted = True

        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter += 1
                already_sorted = False
        if already_sorted:
            break
    return counter


def leftRotateArray():
    """
    A left rotation operation on an array shifts each of the array's
     elements 1 unit to the left. For example, if 2 left rotations are
     performed on array [1, 2, 3, 4, 5], then the array would
     become [3, 4, 5, 1, 2].

    Given an array a of n integers and a number d,perform d left
     rotations on the array. Return the updated array to be
     printed as a single line of space-separated integers.
    ar = [1, 2, 3, 4, 5]
    d = 4
    1,2,3,4,5  ->  2,3,4,5,1  ->  3,4,5,1,2

    Remove the 1st element and adding it to the last
    ar[:len(ar)]
    """
    arr = [1, 2, 3, 4, 5]
    n = 2
    return arr[n:] + arr[:n]


def hourGlassSumIn2DArray():
    """
    Given a  2D Array, :
    1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    0 0 0 0 0 0
    We define an hourglass in  to be a subset of values with indices
    falling in this pattern in 's graphical representation:
    a b c
      d
    e f g
    There are  hourglasses in , and an hourglass sum
    is the sum of an hourglass' values.
    Calculate the hourglass sum for every hourglass in,
    then print the maximum hourglass sum.

    """
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    hour_glass_sum = 0
    max_sum = -float('inf')
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hour_glass_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]
            + arr[i + 2][j + 2]
            max_sum = max(max_sum, hour_glass_sum)
    return max_sum


def isAnagram(s):
    left = 0
    right = n - 1
    while left < right:
        if s[left] != s[right]:
            left += 1
            return False
        right -= 1
        left += 1
    return True


def reverseString(s):
    """
    s = 'corona is real'
    solution 1
    """
    n = len(s) - 1
    new_str = ''
    while n >= 0:
        new_str += s[n]
        n -= 1
    return new_str

    """
    solution 2
    """
    # if len(s) == 0:
    #     return s
    # print(s)
    # return reverseString(s[1:]) + s[1:]


def messageDecode():
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and there are no leading 0’s, no extra trailing 0’s and no two or more consecutive 0’s.
    """
    digits = '1234'
    n = len(digits)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1
    print(count)

    # pos = 0
    # while n - 1 > pos:
    #     if int(message[pos] + message[pos + 1]) < 27:
    #         print(message[pos]  + message[pos + 1])
    #         decodes += 1
    #     pos += 1
    # return decodes + 1

    for i in range(2, n + 1):
        count[i] = 0

        # If the last digit is not 0, then last
        # digit must add to the number of words
        if (digits[i - 1] > '0'):
            count[i] = count[i - 1]
        # If second last digit is smaller than 2
        # and last digit is smaller than 7, then
        # last two digits form a valid character
        if (digits[i - 2] == '1' or
            (digits[i - 2] == '2' and
                digits[i - 1] < '7')):
            print(digits[i - 2])
            count[i] += count[i - 2]

    print(count)
    return count[n]


""""
Fxn that takes a  in a special array and returns it's product sum.
[2,3] = 5
[2,[3, 4, 5]] = 16  w+2x+2y+2z
"""


def productSum(arr, depth=1):
    p_sum = 0
    for i in range(len(arr)):
        if type(arr[i]) == int:
            p_sum += arr[i]
            print (p_sum, depth)
            # print('add')
        else:
            p_sum += productSum(arr[i], depth + 1)
            print(p_sum, depth)
    return p_sum * depth


def permutations():
    arr = [1, 2, 3]
    """
    1,2,3  1,3,2    2,1,3,  2,3,1
    """
    n = len(arr) - 1
    p_arr = []
    while n >= 0:
        print(arr[n])
        p_arr
        n -= 1


def binarySearch(arr, el, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == el:
        return mid
    elif arr[mid] > el:
        return binarySearch(arr, el, start, mid - 1)
    else:
        return binarySearch(arr, el, mid + 1, end)


def missingInteger(A):
    # write your code in Python 3.6
    """"
    Write a function:

    def solution(A)

    that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

    For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

    Given A = [1, 2, 3], the function should return 4.

    Given A = [−1, −3], the function should return 1.

    Write an efficient algorithm for the following assumptions:

    N is an integer within the range [1..100,000];
    each element of array A is an integer within the range [−1,000,000..1,000,000].
    """
    n = len(A)

    if n == 0:
        return 1

    A.sort()
    if A[n - 1] < 1:
        return 1

    if A[0] > 1:
        return 1

    for i in range(n - 1):
        if (A[i + 1] - A[i]) > 1:
            if A[i] < 1:
                return 1
            else:
                return A[i] + 1
    return A[n - 1] + 1


def main():
    # ar = [1, 2, 3, 4, 5]
    # d = 4
    # print(ar, d)
    # s = 'corona is real'
    # arr = [0, 1, 2, 3, 3, 3, 5, 7, 7, 8, 56]
    # print(binarySearch(arr, 5, 0, len(arr) - 1))
    arr = [-9999999999, 1, 2, 3]
    print(missingInteger(arr))


if __name__ == '__main__':
    main()
