"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns.
The robot can only move in two directions, right and down, but certain cells are "off limits" such that
the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to
the bottom right.
"""


def robotInGrid():
    for i in range(10):
        print(i)


# print(robotInGrid())


"""
Unique Paths:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
"""


def uniquePaths():
    m = 3
    n = 2
    matrix = [[1 for i in range(m)] for j in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]

    return matrix[n - 1][m - 1]


def uniquePathsWithObstacles():
    # matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    matrix = [[0, 1], [0, 0]]
    cols = len(matrix[0])
    rows = len(matrix)
    matrix_copy = [[0 for i in range(cols)] for j in range(rows)]
    matrix_copy[0][0] = 1 if matrix[0][0] == 0 else 0

    for i in range(rows):
        for j in range(cols):
            matrix_copy[i][j] = 1
            if matrix[i][j] == 1:
                matrix_copy[i][j] = 0
            else:
                # matrix_copy[i][j] = matrix_copy[i][j - 1] + matrix_copy[i - 1][j]
                print(i, j)
                if i - 1 >= 0:
                    matrix_copy[i][j] += matrix_copy[i - 1][j]
                if j - 1 >= 0:
                    matrix_copy[i][j] += matrix_copy[i][j - 1]
    return matrix_copy[rows-1][cols-1]


"""
Magic Index: A magic index in an array A [ 0 ••• n -1] is defined to be an index such that A[i] = i.
Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in
array A.
FOLLOW UP
What if the values are not distinct?
"""


def magicIndex(arr):
    n = len(arr)
    return binarySearch(arr, 0, n - 1)


def binarySearch(arr, start, end):
    # print(end)
    if end < start:
        return -1
    mid = (start + end) // 2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return binarySearch(arr, start, mid - 1)
    else:
        return binarySearch(arr, mid + 1, end)


# print(magicIndex([-1, 0, 2, 5]))


""""
Power Set: Write a method to return all subsets of a set.
"""


def powerSet():
    pass


"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the
*operator.You can use addition, subtraction, and bit shifting, but you should minimize the number
of those operations.
"""


def recursiveMultiply():
    pass


if __name__ == '__main__':
    print(uniquePathsWithObstacles())
