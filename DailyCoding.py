"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def classRooms():
    arr = [(30, 75), (0, 50), (60, 150)]
    n = len(arr)
    arr.sort()
    room = 0
    # arr = [(0, 50), (30, 75), (60, 150)]
    for i in range(n):
        print(arr[i])
        if arr[i - 1][1] > arr[i][0]:
            room += 1

    print(room)


def fib(n, _cache):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    if n in _cache:
        return _cache[n]
    else:
        _cache[n] = fib(n - 1, _cache) + fib(n - 2, _cache)
        return _cache[n]

# print(fib(100, {}))


def twoNumberSum():
    arr = [1, 2, 3, 4]
    target = 7
    """
    # HASHMAP
    _dict = {}

    for el in arr:
        if el in _dict:
            return [el, _dict[el]]
        _dict[target - el] = el
    return []
    """
    # sort
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            return [arr[left], arr[right]]

    return []


def firstDuplicateLR():
    _dict = {}
    arr = [3, 1, 1, 2, 3, 4]

    for el in arr:
        if el in _dict:
            _dict[el] += 1
        else:
            _dict[el] = 1

    for i in _dict:
        if _dict[i] > 1:
            return i

# print(firstDuplicateLR())


def phoneCombination(digits):
    phone = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

    def backtrack(combination, next_digits):
        # if there is no more digits to check
        if len(next_digits) == 0:
            # the combination is done
            output.append(combination)
        # if there are still digits to check
        else:
            # iterate over all letters which map
            # the next available digit
            for letter in phone[next_digits[0]]:
                # append the current letter to the combination
                # and proceed to the next digits
                backtrack(combination + letter, next_digits[1:])

    output = []
    if digits:
        backtrack("", digits)
    return output

# print(phoneCombination('234'))


def subsequenceCheck():
    arr = [1, 2, 3, 4, 6, 5]
    sub = [0, 1, 5]
    ptr = 0

    for el in arr:
        if el == sub[ptr] and ptr == len(sub) - 1:
            return True
        elif el == sub[ptr]:
            ptr += 1

    return False

print(subsequenceCheck())