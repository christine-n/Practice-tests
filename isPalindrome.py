def isPalindrome(s):
    # boob
    n = len(s)
    if s[0] != s[n-1]:
        return False
    i = 0
    while i < n // 2:
        if s[i] != s[n-1-i]:
            return False
        i+=1
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


def getNthFib(n, memo={1:0, 2:1}):
    # Write your code here.
    if n in memo:
        print(memo)
        return memo[n]
    else:
        memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo)
        print()
        return memo[n]
print(getNthFib(5))
# print(longestPalindrome('somepowophere'))