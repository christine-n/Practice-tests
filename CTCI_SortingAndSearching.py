"""
Sorted Matrix Search:
Given an n x n matrix and a number x, find the position of x in the matrix if it is present in it. Otherwise, print “Not Found”. In the given matrix, every row and column is sorted in increasing order. The designed algorithm should have linear time complexity.
"""


def sortedMatrixSearch():
    arr = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    x = 29
    # for i in range(len(arr)):
    #     for j in range(len(arr)):
    #         if arr[i][j] == x:
    #             return i,j
    n = len(arr)
    i = 0
    j = n - 1

    while i < n and j >= 0:
        if arr[i][j] == x:
            return i,j
        elif arr[i][j] < x:
            i += 1
        else:
            j -= 1
    return 'Not found'

print(sortedMatrixSearch())

