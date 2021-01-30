# Python implementation of above approach

# 2D array for the storing the horizontal and vertical
# directions. (Up, left, down, right
dirs = [[0, -1],
        [-1, 0],
        [0, 1],
        [1, 0]]

# Function to perform dfs of the input grid


def dfs(grid, x0, y0, i, j, v):
    rows = len(grid)
    cols = len(grid[0])

    if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] <= 0:
        return
    # marking the visited element as -1
    grid[i][j] *= -1

    # computing coordinates with x0, y0 as base
    v.append((i - x0, j - y0))

    # repeat dfs for neighbors
    for dir in dirs:
        dfs(grid, x0, y0, i + dir[0], j + dir[1], v)


# Main function that returns distinct count of islands in
# a given boolean 2D matrix
def countDistinctIslands(grid):
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    if cols == 0:
        return 0

    coordinates = set()

    for i in range(rows):
        for j in range(cols):

            # If a cell is not 1
            # no need to dfs
            if grid[i][j] != 1:
                continue

            # to hold coordinates
            # of this island
            v = []
            dfs(grid, i, j, i, j, v)

            # insert the coordinates for
            # this island to set
            print(v)
            coordinates.add(tuple(v))

    return len(coordinates)


# Driver code
grid = [[1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]]

# print("Number of distinct islands is", countDistinctIslands(grid))


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp
    print(arr)


def rotate(arr, d):
    for i in range(d):
        arr.append(leftRotatebyOne(arr, len(arr)))
    return arr

# print(rotate([1,2,3,4, 5], 4))


def minimumSwaps():
    arr = [1, 3, 5, 2, 4, 6, 7]  # ans = 3
    n = len(arr)
    temp = {}
    counter = 0
    for i, val in enumerate(arr):
        temp[val] = i
    print(temp)
    for i in range(n):
        if arr[i] != i + 1:
            counter += 1
            # because they are consecutives, I can see if the number is where it belongs
            t = arr[i]
            arr[i], arr[temp[i + 1]] = i + 1, t
            # Switch also the temp array, no need to change i+1 as it's already good now
            temp[t] = temp[i + 1]

    return counter

def minimumBribes():
    # q = [2, 1, 5, 3, 4] # ans = 3
    q = [1, 2, 5, 3, 7, 8, 6, 4]  # ans = 7
    counter = 0
    for i in range(len(q)):
        distance = q[i] - (i + 1)
        if distance > 2:
            return 'Too chaotic'
        for j in range(len(q[:i]), -1, -1):
            if q[j] > q[i]:
                counter += 1
    return counter


print(minimumBribes())
