#!/bin/python3

import os
import sys

#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    #
    # Write your code here.
    #
    print(indexes)

if __name__ == '__main__':
    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
