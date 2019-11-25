def solution(A):
    n = len(A)
    A.sort()
    result = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1

    for k in range(1, n):
        if A[k] != A[k - 1]:
            result += 1
    return result


def main():
    # [5,5,5,5,5,5,5,5,5,5,5]
    print(solution([5,5,5,5,5,5,5,5,5,5,5]))


if __name__ == '__main__':
    main()
