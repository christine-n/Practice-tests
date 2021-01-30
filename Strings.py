def jump_over_numbers(list):
    pos = 0
    ans = 0
    while pos < len(list):
        if list[pos] == 0:
            return -1
        ans += 1
        pos += list[pos]
        print(pos, ans)

    return ans

# jump_over_numbers([3, 4, 1, 2, 5, 6, 9, 0, 1, 2, 3, 1])
# print(1325132435356//10)


def digit_sum(number):
    # Write your code here
    res = 0
    if number < 0:
        number = number * -1

    while number > 0:
        res += number % 10
        number //= 10
    return res

# print(digit_sum(-1325132435356))


def is_numeric_palindrome(n):
    # Write your code here
    s = str(n)
    n = len(s)

    if s[0] != s[n - 1]:
        return False
    pos = 0
    while pos < n // 2:
        if s[pos] != s[n - 1 - pos]:
            return False
        pos += 1
    return True
# print(is_numeric_palindrome(1221))


# def lexNumbers(x):
#     level = 0
#     files
# lexNumbers(167)

def cyclicRotation(K, A):
    # x = [3, 8, 9, 7, 6] # -> [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
    # [3, 8, 9, 7, 6] , 3  -> [9, 7, 6, 3, 8]
    # [1, 1, 2, 3, 5], 42 -> [3, 5, 1, 1, 2]
    if len(A) == 0:
        return A
    K = K % len(A)
    if K == 0:
        return A

    return (A[-K:] + A[:len(A)-K])
# cyclicRotation([1, 1, 2, 3, 5], 42)

def longes(N):
    bin_str = str(bin(N))
    print(bin_str)
    longest = 0
    counter = 0
    for i in range(2, len(bin_str)):
        print(counter, bin_str[i])
        if bin_str[i] == '1':
            longest = max(counter, longest)
            print(longest, counter)
            counter = 0
        else:
            counter += 1
    print(longest)
longes(1041)

