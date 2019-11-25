def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        raise Exception("Invalid input")
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])


def main():
    print(solution([9, 3, 9, 3, 9, 7, 9]))


if __name__ == '__main__':
    main()
