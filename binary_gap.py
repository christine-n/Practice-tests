def solution():
    N = 1111113446
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


def main():
    print(solution())


if __name__ == '__main__':
    main()
