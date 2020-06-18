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


def sherlockAndAnagrams(s):
    # x = str(s)
    # i = x[len(x)::-1]
    # counter = 0
    # for n in range(len(x)):
    #     if i[n:] == x[n:]:
    #         counter += 1
    #     if i[:len(x) - n] == x[:len(i) - n]:
    #         print()
    #         counter += 1
    # return counter
    n = len(str(s))
    res = 0
    for l in range(1, n):
        cnt = {}
        for i in range(n - l + 1):
            # print(n - l + 1)
            subs = list(s[i:i + l])
            # print(i)
            print(cnt)
            subs.sort()
            subs = ''.join(subs)
            if subs in cnt:
                cnt[subs] += 1
            else:
                cnt[subs] = 1
            res += cnt[subs] - 1
    return res


def main():
    # [5,5,5,5,5,5,5,5,5,5,5]
    # print(solution([5,5,5,5,5,5,5,5,5,5,5]))
    print(sherlockAndAnagrams('baby'))


if __name__ == '__main__':
    main()
