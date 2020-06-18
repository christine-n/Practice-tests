import json

def countSwaps(a):
    arr = len(a)
    count = 0

    for i in range(arr):
        for j in range(arr - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                print(a)
                count += 1
                j += 1
        i += 1

    if count > 1:
        print('Array is sorted in {} swaps.'.format(count))
    else:
        print('Array is sorted in 0 swaps.')

    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))
    print('Array: {}'.format(a))


def maximumToys(prices, k):
    cost = 0
    my_costs = []
    prices.sort()
    i = 0
    print(prices)
    # [1, 5, 10, 12, 111, 200, 1000]

    for i in range(len(prices)):
        if prices[i] <= k:
            cost += prices[i]
            if cost <= k:
                my_costs.append(prices[i])

    print(my_costs)
    return len(my_costs)


def main():
    # print(countSwaps([6, 4, 1]))
    # print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
    # print(maximumToys([1, 2, 3, 4], 7))
    x = "{'date': datetime.date(2019, 1, 10), 'reason': u'The timesheet request has been rejected by your direct manager. Not on project.', 'rejecting_user': u'francis.meyo@busaracenter.org'}"
    print(type(x))
    y = json.loads(x)
    print(type(y))
    print(y['rejecting_user'])


if __name__ == '__main__':
    main()
