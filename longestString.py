# Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

# Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

# Note: D can appear in any format (list, hash table, prefix tree, etc.

# For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

def longestString():
    t = int(input())
    n = []
    for i in range(t):
        n.append(int(input()))

    for i in range(t):
        if n[i] % 21 == 0 or '21' in str(n[i]):
            print('The streak is broken!')
        else:
            print('The streak lives still in our heart!')

    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))


"""
Given an array of numbers, find the length of the longest
increasing subsequence in the array. The subsequence does
not necessarily have to be contiguous.

For example, given the array
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6:
it is 0, 2, 6, 9, 11, 15.
"""


def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)


if __name__ == '__main__':
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(longest_increasing_subsequence(arr))
