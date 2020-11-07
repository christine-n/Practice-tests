def solution(A, B):
    # write your code in Python 3.6
    paths = {}

    if len(A) != len(B):
        return -1

    n = len(A)

    for i in range(n):
        # print(paths)
        if A[i] not in paths:
            paths[A[i]] = B[i]
        else:
            paths[A[i]].append(B[i])
    return paths

print(solution([0,1,2,4,5], [2,3,3,3,2]))