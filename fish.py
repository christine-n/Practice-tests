def solution(A, B):
    # B -> direction
    # A -> size

    for d in range(len(B)):
        if B[d] == 0 and B[d - 1] == 0:
            if A[d - 1] < A[d]:
                A.pop(d - 1)


def main():
    print(solution(A, B))


if __name__ == '__main__':
    main()