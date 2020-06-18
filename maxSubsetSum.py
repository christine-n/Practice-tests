
import math
import os
import random
import re
import sys


def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return max(arr)
    return max([
        arr[0],
        arr[0] + maxSubsetSum(arr[2:]),
        maxSubsetSum(arr[1:])
    ])


if __name__ == '__main__':
    # n = int(input())

    # arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum([2, 1, -8, -5])
    print(res)