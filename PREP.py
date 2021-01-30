"""
a = [1,2,3]
output -> [6, 3, 2]
res = [6, 3, 2 ] -> Time O(n^2) Space O(n)




"""

# import numpy


# def productDict():
#     arr = [1, 2, 3]
#     n = len(arr)
#     dct = {}
#     res = []

#     for i in range(n):
#         dct[arr[i]] = arr[:i] + arr[(i + 1):]
#     print(dct)

#     for i in dct:
#         res.append(numpy.prod(dct[i]))
#     return res


def product():
    arr = [5, 2, 3]
    n = len(arr)
    prod = [1] * n
    left_prod = [1] * n
    right_prod = [1] * n

    # left prod
    l_prod = 1
    for i in range(n):
        left_prod[i] = l_prod
        l_prod *= arr[i]
    print(left_prod)

    # right prod
    r_prod = 1
    for i in reversed(range(n)):
        right_prod[i] = r_prod
        r_prod *= arr[i]
    print(right_prod)

    for i in range(n):
        prod[i] = left_prod[i] * right_prod[i]

    print(prod)


def productV2():
    arr = [5, 2, 3]
    n = len(arr)
    prod = [1] * n

    # left prod
    l_prod = 1
    for i in range(n):
        prod[i] = l_prod
        l_prod *= arr[i]
    print(prod)

    # right prod
    r_prod = 1
    for i in reversed(range(n)):
        prod[i] *= r_prod
        r_prod *= arr[i]

    return prod


def sherlockAndAnagrams(s):
    dct = {}
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            list1 = list(s[i:j].strip())
            list1.sort()
            # print(list1)
            transf = ''.join(list1)
            print(transf)
            if transf in dct:
                count += dct[transf]
                dct[transf] = dct[transf] + 1
            else:
                dct[transf] = 1
            # print(dct, count)
    return count
# print(sherlockAndAnagrams('abcda'))


def countTriplets():
    arr = [1, 4, 16, 64]
    r = 4
    if len(arr) <= 2:
        return 0
    map_arr = {}
    map_doubles = {}
    count = 0
    # Traversing the array from rear, helps avoid division
    for x in arr[::-1]:

        r_x = r * x
        r_r_x = r * r_x

        # case: x is the first element (x, x*r, x*r*r)
        count += map_doubles.get((r_x, r_r_x), 0)

        # case: x is the second element (x/r, x, x*r)
        map_doubles[(x, r_x)] = map_doubles.get(
            (x, r_x), 0) + map_arr.get(r_x, 0)

        # case: x is the third element (x/(r*r), x/r, x)
        map_arr[x] = map_arr.get(x, 0) + 1
        print(map_doubles, map_arr)

    return count

# print(countTriplets())


def arrSubsequence():
    # arr b a subsequence of a
    a = [1, 2, 3, 4]
    b = [1, 2]  # true
    # b = [2, 4]  # true
    # b = [1, 2, 5]  # false
    # b = [2,1]  # false
    n = len(a)
    m = len(b)
    i, j = 0, 0

    if m > n:
        return False

    while i < n and j < m:
        if a[i] == b[j]:
            j += 1
        i += 1
    if j == m:
        return True

    return False

# print(arrSubsequence())


def tripletSumTarget():
    array = [12, 3, 1, 2, -6, 5, -8, 6]  # [-8, -6, 1, 2, 3, 5, 6, 12]

    targetSum = 0
    res = []
    # outputs = [[-8,2,6], [-8,3,5], [-6,1,5]]
    array.sort()
    n = len(array)
    for i in range(n):
        left = i + 1
        right = n - 1
        while left < right:
            if array[i] + array[left] + array[right] > targetSum:
                right -= 1
            elif array[i] + array[left] + array[right] < targetSum:
                left += 1
            else:
                res.append([array[i], array[left], array[right]])
                right -= 1
                left += 1
    return res

# print(tripletSumTarget())


def commonChild(s1, s2):
    # 'HARRY', 'SALLY' -> 2
    # 'SHINCHAN', 'NOHARAAA' -> 3
    n = len(s1)
    matrix = [[0 for _ in range(n + 1)]for _ in range(n + 1)]
    """
    [  H A R R Y
     [0,0,0,0,0,0]
   S [0,0,0,0,0,0]
   A [0,0,1,1,1,1]
   L [0,1,1,1,0,0]
   L [0,0,0,0,1,1]
   Y [0,1,0,0,1,2]
    ]

    [   S  H  I  N  C  H  A  N
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
   N [0, 0, 0, 0, 0, 0, 0, 0, 0],
   O [0, 0, 0, 1, 1, 1, 1, 1, 1],
   H [0, 0, 0, 1, 1, 1, 1, 1, 1],
   A [0, 1, 1, 1, 1, 1, 1, 1, 1],
   R [0, 1, 1, 1, 1, 1, 1, 1, 1],
   A [0, 1, 1, 2, 2, 2, 2, 2, 2],
   A [0, 1, 1, 2, 3, 3, 3, 3, 3],
   A [0, 1, 1, 2, 3, 3, 3, 3, 3]]
    """
    for r in range(n):
        for c in range(n):
            if s2[c] == s1[r]:
                matrix[r + 1][c + 1] = matrix[r][c] + 1
            else:
                matrix[r + 1][c + 1] = max(matrix[r + 1][c], matrix[r][c + 1])
    print(matrix)
    return matrix[n][n]

# print(commonChild('SHINCHAN', 'NOHARAAA'))


def superReducedString(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            print(s)
            s = s[:i] + s[i + 2:]
            i = 0
        else:
            i += 1

    return s if s else 'Empty String'


# print(superReducedString("baab"))

"""
Move el to end

arr = [2,1,2,2,2,3,4,2]
d = 2
output=[1,3,4,2,2,2,2,2]
"""


def moveToEnd():
    # arr = [2, 1, 2, 2, 2, 3, 4, 2]
    arr = [4, 1, 3, 2, 2, 2, 2, 2]
    d = 2
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[right] == d:
            right -= 1
        elif arr[left] == d:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1
            right -= 1
        else:
            left += 1
    return arr

# print(moveToEnd())


def introTutorial(V, arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[right] == V:
            return right
        elif arr[left] == V:
            return left
        elif arr[left] < V:
            left += 1
        elif arr[right] > V:
            right -= 1
    return
print(introTutorial(5, [1, 4, 5, 7, 9, 12]))