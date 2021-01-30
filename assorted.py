#!/usr/bin/env python
import collections
import sys
import math
from typing import List


def find_longest_word_in_string(letters, words):
    print(letters)


def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * (i))


def fibonacciMemo(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        to_return = 1
    else:
        for i in range(n):
            to_return = fibonacciMemo((n - 1), memo) + fibonacciMemo(n - 2, memo)  # noqa
        memo[n] = to_return
    return to_return


def fibonnacciBottomUp(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


def fib(n):
    # memoization
    # memo = [None] * (n + 1)
    # print(fibonacciMemo(n, memo))

    # bottom up approach
    print(fibonnacciBottomUp(n))


def fibonacciModified(t1, t2, n):
    a = t1
    b = t2
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            # c = a + (b*b)
            # a = b
            # b = c
            a, b = b, a + b
        return b


def staircaseFib(n, X):
    cache = [0 for _ in range(n + 1)]  # or simply cache = [0] * (n + 1)        # noqa
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x > 0)
        cache[i] += 1 if i in X else 0
    return cache[-1]   # or simply cache[n]


def maxSubarray():
    # arr = [ -2, -3, -1, -4, -6]
    arr = [1, 2, -1, 3, 4]
    """
    In the first case: The maximum sum for both types of subsequences is just the sum of all the elements since they are all positive.
    input:- [2, -1, 2, 3, 4, -5]
    In the second case: The subarray [2, -1, 2, 3, 4] is the subarray with the maximum sum of 10, and [2, 2, 3, 4] is the subsequence with the maximum sum of 11.
    output:- [10, 11]
    """
    sum_arr = [arr[0], arr[0]]
    current_sum = arr[0]
    for x in range(1, len(arr)):
        #  the maximum subarray sum
        current_sum = max(arr[x], (current_sum + arr[x]))
        sum_arr[0] = max(sum_arr[0], current_sum)

        # the maximum subsequence sum

        if sum_arr[1] < arr[x] and arr[x - 1] < 0:
            sum_arr[1] = arr[x]
        else:
            sum_arr[1] = max((sum_arr[1] + arr[x]), sum_arr[1])

    return sum_arr


def stockmax(prices):
    # prices=[5, 3, 2] profit = 0
    # prices = [1, 2, 0, 100] profit = 197

    n = len(prices)
    profit = 0
    maxprice = prices[n - 1]

    if n <= 1:
        return (0)
    else:
        """
        start from future and keep track of max price.
        If current price is less than max price then buy it
        profit+=maxprice-current price.
        """
        for i in range(n - 1, -1, -1):
            if maxprice < prices[i]:
                maxprice = prices[i]
            elif prices[i] < maxprice:
                profit += (maxprice - prices[i])
        return profit


def substrings(n):
    # The sub-strings of 123 are 1, 2, 3, 12, 23, 123 which sums to 164.
    s = str(n)

    # Using String Comprehension
    # long way
    res = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            res.append(int(s[i: j]))

    # Short-hand
    # res = [int(s[i: j]) for i in range(len(s)) for j in range(i + 1, len(s) + 1)]   # noqa

    return sum(res) % (10**9 + 7)


def coinChange():
    n = 4
    coins = [1, 2, 3]


def binarySearch():
    arr = [1, 2, 4, 5, 10]
    target = 5
    n = len(arr)
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def rec_count_ways(arr, target, i, cache):
    key = str(target) + ':' + str(i)
    # print(key)
    if key in cache:
        print('key')
        return cache[key]
    elif target == 0:
        return 1
    elif target < 0:
        return 0
    elif i < 0:
        return 0
    elif target < arr[i]:
        to_return = rec_count_ways(arr, target, i - 1, cache)
    else:
        to_return = rec_count_ways(
            arr, target - arr[i], i - 1, cache) + rec_count_ways(arr, target - arr[i], i - 1, cache)  # noqa
    return to_return


def count_ways():
    arr = [2, 4, 6, 10]
    target = 16
    cache = {}
    return rec_count_ways(arr, target, len(arr) - 1, cache)


def lonelyinteger():
    a = [0, 0, 1, 2, 1]
    my_list = {}
    for i in a:
        if i not in my_list:
            my_list[i] = 1
        else:
            my_list[i] += 1

    for key, value in my_list.items():
        if value == 1:
            return key


def icecreamParlor():
    m = 4
    arr = [1, 4, 5, 3, 2]
    # arr = [2, 2, 4, 3]
    s = {}
    for i in range(len(arr)):
        if m - arr[i] in s:
            return [s[m - arr[i]], i + 1]
        else:
            s[arr[i]] = i + 1
            print(s)


def trap(height):
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    if not height:
        return 0
    n = len(height)
    lm, rm = [0] * n, [0] * n
    lm[0], rm[-1] = height[0], height[-1]

    for i in range(1, n):
        lm[i] = max(lm[i - 1], height[i])

    for i in range(n - 2, -1, -1):
        rm[i] = max(rm[i + 1], height[i])

    ans = 0
    for i in range(n):
        ans += max(0, min(lm[i], rm[i]) - height[i])
    return ans


def maxArea(height):
    lmax = height[0]
    rmax = height[-1]
    n = len(height)
    left = area = 0
    right = n - 1
    while left <= right:
        if height[left] < height[right]:
            area = max(area, (height[left] * (right - left)))
            left += 1
        else:
            area = max(area, (height[right] * (right - left)))
            right -= 1
    return area


def productExceptSelf(nums):
    n = len(nums)
    # Base case
    if n == 1:
        print(0)
        return

    i, temp = 1, 1

    # Allocate memory for the product array
    prod = [1 for i in range(n)]

    # Initialize the product array as 1

    # In this loop, temp variable contains product of
    # elements on left side excluding nums[i]
    for i in range(n):
        prod[i] = temp
        temp *= nums[i]
    print(prod)
    # Initialize temp to 1 for product on right side
    temp = 1

    # In this loop, temp variable contains product of
    # elements on right side excluding nums[i]
    for i in range(n - 1, -1, -1):

        prod[i] *= temp
        temp *= nums[i]

    # Print the constructed prod array
    for i in range(n):
        prod[i]
    return prod


def maxProduct(nums):
    n = len(nums)
    curMax = minusMax = globalMax = nums[0]
    for i in range(1, n):
        nextMinusMax = minusMax * nums[i]
        nextCurMax = curMax * nums[i]
        minusMax = min(nextMinusMax, nextCurMax, nums[i])
        curMax = max(nextCurMax, nextMinusMax, nums[i])
        globalMax = max(globalMax, curMax)
    return globalMax


def lengthOfLongestSubstring(s):
    # s= "pwwkew" # 3
    # s ="abcabcbb" # 3
    s = " "  # 1
    # s = "bbbbb" # 1
    # s = "dvdf" # 3
    # n = len(s)
    # max_len = counter = 0
    # curr = []

    # if n == 0:
    #     return 0
    # elif n == 1:
    #     return 1
    # my trial
    # for i in range(n):
    #     print(curr)
    #     if s[i] not in curr:
    #         curr.append(s[i])
    #     else:
    #         curr = []
    #         curr.append(s[i])
    #     max_len = max(len(curr), max_len)
    # return max_len
    lst = []
    for c in s:
        lst.append(c)
        if len(set(lst)) < len(lst):
            lst.pop(0)
    return len(lst)


def findMedianSortedArrays(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    nums3 = []
    counter = 0
    x = m + n
    mid = x // 2 if x % 2 != 0 else x // 2 + 1

    while m - 1 > 0 and n - 1 > 0 and (m <= mid or n <= mid):
        if nums1[m] <= nums2[n]:
            nums3.append(nums1[m])
            m -= 1
        elif nums1[m] <= nums2[n]:
            nums3.append(nums2[m])
            n -= 1
        if mid == m:
            return nums1[-1]
        elif mid == n:
            return nums2[-1]


def myAtoi(s):
    # num = ''
    # s = s.strip()
    # if s[0] not in ['-', '+'] and not s[0].isdigit():
    #     return 0

    # for c in s:
    #     if c in ['-', '+'] or c.isdigit():
    #         num += c
    #     else:
    #         break

    # if abs(int(num)) > 2**31:
    #     return -2**31 if num[0] == '-' else 2**31
    # else:
    #     return int(num)
    s = s.strip()
    if len(s) == 0:
        return 0
    res, sign, st = 0, 0, 0
    for c in s:
        if c.isdigit():
            res = res * 10 + int(c)
            print(c, res * 10)
        elif c == '-' and not st:  # if c is '-' and there is nothing before it
            if sign != 0:
                break
            else:
                sign = -1
        elif c == '+' and not st:  # if c is '+' and there is nothing before it
            if sign != 0:
                break
            else:
                sign = 1
        else:
            break  # c is not valid char
        st = True
    if sign == -1:
        return max(-2**31, -res)
    return min(2**31 - 1, res)


def smallestDivisor():
    # Input: nums = [2,3,5,7,11], threshold = 11
    # Output: 3
    # Input: nums = [1,2,5,9], threshold = 6
    # Output: 5
    # Input: nums = [19], threshold = 5
    # Output: 4

    nums = [1, 2, 5, 9]
    threshold = 6
    def compute_sum(x): return sum([math.ceil(n / x) for n in nums])  # noqa
    """
    Solution 1
    """
    # d = 1
    # while compute_sum(d) > threshold:
    #     d += 1
    # return d

    """
    Solution 2
    """
    left = 1
    right = max(nums)
    while left <= right:
        pivot = (right + left) // 2
        num = compute_sum(pivot)
        if num > threshold:
            left = pivot + 1
        else:
            right = pivot - 1
    return left


def birthday():
    # s = [1, 2, 1, 3, 2]
    # d = 3
    # m = 2
    s = [4]
    d = 4
    m = 1
    # s = [1, 1, 1, 1, 1, 1]
    # d = 3
    # m = 2
    n = len(s)
    count = 0
    nums = []

    if n == 1 and m == 1 and d == s[0]:
        return 1

    for i in range(n - m):
        if sum(s[i:(i + m)]) == d:
            count += 1
            nums.append(s[i:(i + m)])
    return count


def twoSum():
    # nums = [2, 7, 11, 15]
    # target = 9

    nums = [3, 2, 4]
    target = 6
    n = len(nums)
    dct = {}
    for i in range(n):
        diff = target - nums[i]
        if diff in dct:
            return [i, dct[diff]]
        else:
            dct[nums[i]] = diff
    return []


def addBinary(a: str, b: str) -> str:
    print(a, b)
    m = len(a) - 1
    n = len(b) - 1
    res = ''
    carry = 0

    while m >= 0 or n >= 0:
        one = 0 if m < 0 else a[m]
        two = 0 if n < 0 else b[n]
        _sum = int(one) + int(two) + carry
        carry = 1 if _sum > 1 else 0
        _sum = 0 if _sum < 1 else _sum % 2
        res += (str(_sum))
        print(res)

        m -= 1
        n -= 1
    if carry > 0:
        res += (str(carry))
    return res[::-1]


def isPalindrome(s: str) -> bool:
    n = len(s)
    left = 0
    right = n - 1
    if n <= 1:
        return False
    while left < right:
        if s[left] != s[right]:
            return False
    return True


def longestPalindrome(s: str) -> str:
    pals = {}
    n = len(s)
    start = 0
    end = n - 1
    # pal = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)) if isPalindrome(s[i:j]) ]
    for i in range(start, n):
        pass

    print(pals)
    return ''


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n, counter = 0, 0, 0
    nums3 = []
    x = len(nums1) + len(nums2)
    is_decimal = False if x % 2 == 0 else True
    mid = x // 2
    l = len(nums1) if len(nums1) < len(nums2) else len(nums2)
    print(l)
    while len(nums3) <= mid:
        print(mid, len(nums3))
        if nums1[m] < nums2[n]:
            nums3.append(nums1[m])
            m += 1
        else:
            nums3.append(nums2[n])
            n += 1
    print(nums3)
    # if is_decimal:
    #     return (nums3[-1] + nums3[-2]) / 2
    # return nums3[-1]

def twoSum(numbers: List[int], target: int) -> List[int]:
    # numbers = [2,3,4], target = 6 Output: [1,3]
    # numbers = [2,7,11,15], target = 9 Output: [1,2]
    dct = {}
    for idx, val in enumerate(numbers):
        diff = target - val
        if diff in dct:
            return [dct[diff], idx + 1]

        dct[val] = idx + 1



if __name__ == '__main__':
    D = {"able", "ale", "apple", "bale", "kangaroo"}
    S = "abppplee"

    # print (find_longest_word_in_string(S, D))
    # print(fibonacciModified(0, 1, 5))
    # print(substrings(123))
    # print(stockmax([5, 3, 2]))
    # fib(1000)
    # print(findMedianSortedArrays([1, 2, 3], [1, 2, 3]))
    # print(twoSum())
    # print(addBinary("0", "0"))
    # print(longestPalindrome('abppplee'))
    # findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4])
    print(twoSum(numbers = [2,3,4], target = 6))
