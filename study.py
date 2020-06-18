def minimumSwap():
    """
    You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

    For example, given the array arr=[7, 1, 3, 2, 4, 5, 6] we perform the following steps:
    i   arr                     swap (indices)
    0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
    1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
    2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
    3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
    4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
    5   [1, 2, 3, 4, 5, 6, 7]
    It took 5 swaps to sort the array.

    Function Description

    Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.

    minimumSwaps has the following parameter(s):

    arr: an unordered array of integers
    Given array arr [1, 3, 5, 2, 4, 6, 7]
    After swapping (1,3) we get [1, 2, 5, 3, 4, 6, 7]
    After swapping (2,3) we get [1, 2, 3, 5, 4, 6, 7]
    After swapping (3,4) we get [1, 2, 3, 4, 5, 6, 7]
    """
    arr = [2, 1, 3, 7, 4, 5, 6]
    # binary search
    n = len(arr)
    for i in range(n):
        already_sorted = True
        print('\n')
        for j in range(n-1):
            print(arr[j], arr[j+1])
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False
            print(arr)
        if already_sorted:
            break
    return arr




def leftRotateArray():
    """
    A left rotation operation on an array shifts each of the array's elements 1 unit to the left. For example, if 2 left rotations are performed on array [1, 2, 3, 4, 5], then the array would become [3, 4, 5, 1, 2].

    Given an array a of n integers and a number d,perform d left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.
    ar = [1, 2, 3, 4, 5]
    d = 4
    1,2,3,4,5  ->  2,3,4,5,1  ->  3,4,5,1,2

    Remove the 1st element and adding it to the last
    ar[:len(ar)]
    """
    arr = [1, 2, 3, 4, 5]
    n = 2
    i = 0
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
    There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.
    Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

    """
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]
    hour_glass_sum = 0
    max_sum = -float('inf')
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hour_glass_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_sum = max(max_sum, hour_glass_sum)
    return max_sum



def main():

    ar = [1, 2, 3, 4, 5]
    d = 4

    # print(ar, d)
    print(minimumSwap())


if __name__ == '__main__':
    main()
