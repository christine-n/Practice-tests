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

print(fib(100, {}))
