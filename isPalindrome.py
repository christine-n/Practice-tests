def isPalindrome(s):
    # boob
    n = len(s)
    if s[0] != s[n - 1]:
        return False
    i = 0
    while i < n // 2:
        if s[i] != s[n - 1 - i]:
            return False
        i += 1
    return True


def longestPalindrome(s):
    # somepowophere
    n = len(s)
    longestPd = ''
    for i in range(n):
        ns = ''
        for j in range(i, n):
            ns = ns + s[j]
            if isPalindrome(ns):
                if len(ns) > len(longestPd):
                    longestPd = ns
    return longestPd


def isNumberPalindrome(x):
    # without conerting the int to string
    revertedNumber = 0
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    elif x >= 0 and x < 10:
        return True
    else:
        while (x > revertedNumber):
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
            print(x, revertedNumber)

    return x == revertedNumber or x == revertedNumber // 10


def is_numeric_palindrome(n):
    arr = []
    while(n > 0):
        arr.append(n % 10)
        n = n // 10

    num_len = len(arr)
    for i in range(num_len / 2):
        if arr[i] != arr[num_len - i - 1]:
            return False

    return True


def getNthFib(n, memo={1: 0, 2: 1}):
        # Write your code here.
    if n in memo:
        print(memo)
        return memo[n]
    else:
        memo[n] = getNthFib(n - 1, memo) + getNthFib(n - 2, memo)
        print()
        return memo[n]
# print(getNthFib(5))

# print(longestPalindrome('somepowophere'))

# print(isNumberPalindrome(2112))


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    isNegative = False
    rev = 0
    if x < 0:
        isNegative = True
        x = x * -1

    while x:
        # rem = x%10
        rev = rev * 10 + x % 10
        x = x // 10

    return rev if not isNegative else rev * -1
# print(reverse(-11))


def intToRoman(num: int) -> str:
    count = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100],
             ['XC', 90], ['L', 50], ['XL', 40], ['X', 10], ['IX', 9],
             ['V', 5], ['IV', 4], ['I', 1]]
    result = ""
    for x in count:
        print(num, x)
        result += x[0] * (num // x[1])
        print(result)
        num = num % x[1]
    return result


# print(intToRoman(123))


def searchInsert(nums, target):
    # [1,3,5,6], 7
    # [1,3,5,6], 2
    n = len(nums)
    left = 0
    right = n - 1
    if target < nums[0]:
        return 0
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return left

print(searchInsert([1,3,5,6], 2))
