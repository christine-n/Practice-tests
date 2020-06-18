#!/bin/python3

from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(ar):
    sum = 0
    for values in Counter(ar).values():
        sum += values//2
    return sum

def countingValleys(ar):
    valleys = 0
    count = 0

    for i in range(len(ar)):
        if (ar[i]=='U' ):
            count += 1
        else:
            if (count == 0):
                valleys+=1
            count -= 1

    return valleys


def getMoneySpent(keyboards, drives, b):
    money = 0
    arr = []
    total = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            total = drives[j] + keyboards[i]
            if (total <= b):
                arr.append(total)
    if (len(arr) == 0):
        return -1
    else:
        return max(arr)


def kangaroo(x1, v1, x2, v2):
    if (v1 > v2):
        remainder = (x1 - x2) % (v2 - v1)
        if (remainder == 0):
            return 'YES'
    return 'NO'


def jumpingOnClouds(c, k):
    if


if __name__ == '__main__':
    # sockMerchant
    # ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    # result = sockMerchant(ar)

    # countingValleys
    # ar = ['U','D','D','D','U','D','U','U']
    # countingValleysResult = countingValleys(ar)
    # print(countingValleysResult)

    # getMoneySpent
    # result = getMoneySpent([40,50,60],[5,8,12],60)

    result = kangaroo(0,3,4,2)

    print(result)
