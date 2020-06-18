# It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people Qd up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by  from  at the front of the line to  at the back.

# Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if  and  bribes , the queue will look like this: .

# Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!
#!/bin/python3
import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
def minimumBribes(Q):
    lastIndex = len(Q) - 1
    bribes, comps = 0, 0
    swaped = False


    # check if the Q is too chaotic
    for i, v in enumerate(Q):
        if (v - 1) - i > 2:
            return "Too chaotic"
    # bubble sorting to find the answer
    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            comps += 1
            if Q[j] > Q[j+1]:
                temp = Q[j]
                Q[j] = Q[j+1]
                Q[j+1] = temp
                bribes += 1
                swaped = True

        if swaped:
            swaped = False
        else:
            break
    return bribes


def main():
    # t = int(input())
    # for t_itr in range(t):
    #     n = int(input())

    #     q = list(map(int, input().rstrip().split()))
    print(minimumBribes([2,5,1,3,4]))

if __name__ == '__main__':
    main()