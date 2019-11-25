def solution(N):
    arr_size = len(N)
    for i in range(0, arr_size):
        count = 0
        for j in range(0, arr_size):
            if N[i] == N[j]:
                count += 1
        if (count % 2 != 0):
            return N[i]


# best solution
def solutionHashing(N):
    # Initialize result
    res = 0

    # Traverse the array
    for element in N:
        # XOR with the result
        res = res ^ element

    return res


def main():
    print(solution([9, 3, 9, 3, 9, 7, 9]))


if __name__ == '__main__':
    main()
