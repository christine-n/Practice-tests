def solution(N):
    # write your code in Python 3.6
    print(str(bin(N)[2:]))
    data = str(bin(N)[2:])
    i = 0
    counter = 0
    gap = 0
    for i in range(len(data)):
        print(data[i])
        if data[i] == '1':
            gap = max(gap, counter)
            counter = 0
        else:
            counter += 1
    return gap


def fizzBuzz():
    nums = 100
    for num in range(1, nums):
        if num % 3 == 0 and num % 5 == 0:
            print('{} fizz buzz'.format(num))
        elif num % 3 == 0:
            print('{} fizz'.format(num))
        elif num % 5 == 0:
            print('{} buzz'.format(num))
        else:
            print('Not divisible by either')

def solution(A):
    # write your code in Python 3.6
    max_p = float('-inf')
    max_subP = float('-inf')
    n = len(A)
    nums = []
    for i in range(n):
        left = i + 1
        right = n - 1
        # print(left, right)
        while left < right:
            max_subP = max((A[left] * A[right]), max_subP)
            left += 1
            right -= 1
            print(max_subP)

        max_prod =max(max_subP, (max_subP * i))

    return max_prod


def main():
    print(solution([-3, 1, 2, -2, 5, 6]))


if __name__ == '__main__':
    main()
