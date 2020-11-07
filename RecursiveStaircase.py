"""
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.



"""



def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        print(countWays(n - 1), countWays(n - 2))
        return countWays(n - 1) + countWays(n - 2)


def ways(n):
    count = 2
    return countWays(n)


# print(ways(10))

def fibonnaciIterative(n):
    if n < 2:
        return n
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a, b = b, c

    return (a + b)


def fibonacciRecursive(n, memo):
    if n in memo:
        return memo[n]
    elif n < 2:
        return n
    else:
        memo[n] = fibonacciRecursive(n - 1, memo) + fibonacciRecursive(n - 2, memo)
    print(memo)
    return memo[n]


def fib(n):
    memo = {}
    return fibonnaciIterative(n)


print(ways(4))
