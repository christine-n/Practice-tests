def fizzBuzz(n):
    # Write your code here
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

def countGroups(related):
    # Write your code here
    n = len(related)
    counter = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                if related[i][j] == '1':
                    counter+=1
    print(counter)


# countGroups(['10000','01000','00100','00010','00001'])

def fiveStarReviews(productRatings, ratingThreshold):
    # Write your code here
    n = len(productRatings)
    if (sum([i[0]/i[1] for i in productRatings])/n) * 100 >= ratingThreshold:
        return 0
    count = 1
    for i in range(n - 1):
        if productRatings[i][0] != productRatings[i][1]:
            productRatings[i][0] += 1
            count += 1
            if (sum([i[0]/i[1] for i in productRatings])/n) * 100 >= ratingThreshold:
                return count

print(fiveStarReviews([[1, 2], [1, 3]], 50))
# 5

# >>> matrix = [[1,2,3,4],
# ...           [2,3,4,5],
# ...           [3,4,5,6],
# ...           [4,5,6,7]]
# >>> N = 4
# >>>

# [
# [related[y-x][x]
# for x in range(N) if 0<=y-x<N
# ]
# for y in range(2*N-1)
# ]