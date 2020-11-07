def appleTrees(arr, n, m):
    curr = {}
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'A':
                curr = {str(1) + ':' + str(2)}
    print(arr, n, m)


def coins(n, arr):
    arr = [1, 6, 4, 8, 11, 16]
    n = len(arr)
    largest = max(arr)
    counter = 0
    max_count = 0

    for i in range(n):
        largest = max(arr[i], largest)
        counter += 1
        if counter % 2 != 0:
            max_count += largest
            largest = 0
    return max_count


def smaller(n, arr):
    c_arr = arr
    ans = []
    for i in range(n):
        if i < max(c_arr):
            # print(ans)
            ans.append(max(c_arr))
            index = arr.index(max(c_arr))
            x = c_arr.pop(index)
            print(x)
        elif i >= min(c_arr):
            ans.append(int(-1))

    return ans


def isAnagram():
    words = ['cinema', 'foo', 'iceman', 'ofo']
    dct = {}
    for word in words:
        ang = ''.join(sorted(word))
        print(ang)
        if ang in dct:
            dct[ang].append(word)
        else:
            dct[ang] = [word]
    return list(dct.values())


if __name__ == '__main__':
    # t = input()
    # n = input()
    # arr = []
    # for i in input().split():
    #     arr.append(int(i))
    # print(coins())
    # print(smaller(7, [5, 1, 9, 2, 5, 1, 7]))
    print(isAnagram())
# 9 -1 5 7 7 -1 -1


# if __name__ == '__main__':
#     t = input()
#     n, m = input().split()
#     arr = input()
#     # print(appleTrees(arr, n, m))
