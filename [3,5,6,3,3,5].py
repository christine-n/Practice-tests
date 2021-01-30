def longestSubArray():
    """
    Longest consecutive sub array of sum x
    """
    given_sum = 10
    arr = []
    n = len(arr)
    max_length = 0

    for i in range(n):
        arrSum = arr[i]
        for j in range(i + 1, n):
            arrSum += arr[j]
            if arrSum == given_sum:
                cur_length = (j + 1) - i
                max_length = max(max_length, cur_length)
    return max_length


def pairs():
    arr = [3, 5, 6, 3, 3, 5]
    n = len(arr)
    pairs = {}
    for i in range(n):
        if arr[i] in pairs:
            pairs[arr[i]] += 1
        else:
            pairs[arr[i]] = 1
    ans = 0
    for it in pairs:
        count = pairs[it]
        ans += (count * (count - 1)) // 2
    return ans


def binStringIter():
    s = '011100'
    val = int(s, 2)
    counter = 0

    while val > 0:
        if val % 2 == 0:
            val = val // 2
            counter += 1
        else:
            val -= 1
            counter += 1
    return counter


def binStringRec(val, counter):
    if val == 0:
        return counter

    if val % 2 == 0:
        val = val // 2
        counter += 1
    else:
        val -= 1
        counter += 1
    return binStringRec(val, counter)


def binString():
    s = '01100'
    val = int(s, 2)
    print(val)
    counter = 0
    return binStringRec(val, counter)
print(binString())

def toLowestIntVal():
    i = 20
    s = str(i)

    if i < 1:
        return 0
    if len(s) == 1:
        return 0

    return int(s[0]) * 10**(len(s) - 1)


"""
longest peak
"""


def longestPeak():
    # arr = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    # arr = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
    arr = [1, 1, 3, 2, 1, 4, 5]
    # arr = [1, 3, 2]
    # arr = [1, 2, 3, 3, 2, 1]
    longest = 0
    start = 0
    increasing = False
    decreasing = False

    for i in range(len(arr) - 1):
        if arr[i] < arr[i + 1] and not increasing:  # increasing
            increasing = True
            start = i
        elif arr[i] > arr[i + 1] and increasing:  # Should be decreasing
            decreasing = True
            increasing = False
        if increasing and decreasing:  # finished peak
            longest = max(longest, (i + 1 - start) + 1)
            decreasing = False
            print(start, i)
            start = i

    return longest


def sumSubArrays():
    """
    Consecutive sub arrays that add to zero
    """
    # arr = [-2, -1, 0, 1, 2, 3]
    arr = [4, 2, -3, -1, 0, 4]
    # arr.sort()
    n = len(arr)
    sub_arr = []

    for i in range(n):
        _sum = arr[i]
        if _sum == 0:
            sub_arr.append([arr[i]])
        for j in range(i + 1, n):
            _sum += arr[j]
            print(i, j, arr[j], _sum)
            if _sum == 0:
                sub_arr.append(arr[i:j + 1])
    return sub_arr
# def solution(S):
#     # write your code in Python 3.6
#     count = 0
#   newS = S[0]

#   n = len(S)
#   for i in range(1,len(S)):
#     if isOrder(newS, S[i]):
#       newS = newS + S[i]
#     else:
#       count += 1
#   return min(count, n-count)


# def isOrder(s,e):
#   if s[-1] == 'A' and e == 'B':
#     return True
#   elif s[-1] == 'A' and e == 'A':
#     return True
#   elif s[-1] == 'B' and e == 'B':
#     return True
#   else:
#     return False

    # right = 0
    # left = 0
    # maxD = 0
    # for i in range(n - 1):
    #     if blocks[i + 1] >= blocks[i] and i + 1 != n - 1:
    #         continue
    #     elif blocks[i + 1] < blocks[i]:
    #         print(blocks[i])
    #         right = i
    #         cur = right - left + 1
    #         maxD = max(maxD, cur)
    #         # reset left and right
    #         left = i + 1
    #         right = i + 1
    #     else:
    #         # last element
    #         right = n - 1
    #         cur = right - left + 1
    #         maxD = max(maxD, cur)
    # return maxD

def solution():
    # blocks = [2, 6, 8, 5]
    blocks = [1, 5, 5, 2, 6]
    n = len(blocks)
    max_distance = 0
    for i in range(n - 1):
        left = i
        right = i + 1
        distance = 0
        while left < right:
            # print(blocks[left], blocks[i], blocks[right])
            print(left, i, right)

            if blocks[left] <= blocks[left - 1]:
                distance += 1
                left -= 1
                print('left')
            elif blocks[right] <= blocks[right - 1] and right < n - 1:
                # print(blocks[right])
                distance += 1
                right += 1
                print('right')
            else:
                print('here')
                # left -= 1
                # right += 1
                break

            print(distance)
            # print(max_distance)
            max_distance = max(max_distance, distance)
    return max_distance


# print(solution())
