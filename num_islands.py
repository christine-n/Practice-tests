from typing import List
"""
Count number of islands
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


def islandToWater(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
        return
    grid[i][j] = '0'
    islandToWater(grid, i - 1, j)
    islandToWater(grid, i + 1, j)
    islandToWater(grid, i, j - 1)
    islandToWater(grid, i, j + 1)


def numIslands(grid: List[List[str]]) -> int:
    counter = 0
    if len(grid) == 0:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                counter += 1
                islandToWater(grid, i, j)

    return counter


"""
Distinct islands
"""


def getIslands(grid, x0, y0, i, j, coordinates):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
        return

    if grid[i][j] == '1':
        coordinates.append((i - x0, j - y0))

    grid[i][j] = '0'
    getIslands(grid, x0, y0, i - 1, j, coordinates)
    getIslands(grid, x0, y0, i + 1, j, coordinates)
    getIslands(grid, x0, y0, i, j - 1, coordinates)
    getIslands(grid, x0, y0, i, j + 1, coordinates)


def numDistinctIslands(grid: List[List[str]]) -> int:
    islands = set()
    if len(grid) == 0:
        return 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                coordinates = []
                getIslands(grid, i, j, i, j, coordinates)
                print(coordinates)
                islands.add(tuple(coordinates))

    return len(islands)


if __name__ == '__main__':
    # isl = [
    #           ["1", "1", "0", "0", "0"],
    #           ["1", "1", "0", "0", "0"],
    #           ["0", "0", "1", "0", "0"],
    #           ["0", "0", "0", "1", "1"]
    #         ]
    isl = [[ "1", "1", "0", "1", "1" ],
            [ "1", "0", "0", "0", "0" ],
            [ "0", "0", "0", "0", "1" ],
            [ "1", "1", "0", "1", "1" ] ]
    # print(numDistinctIslands(isl))


def segment(x, space):
    segments = []
    # for i in range(len(space)):
    #     segment = space[i:i + x]
    #     if len(segment) == x:
    #         segments.append(min(space[i:i + x]))
    i = 0
    n = len(space)
    if x == 1:
        return max(space)
    while i < n - x:
        segment = space[i: i + x]
        segments.append(min(segment))
        i += 1
    return max(segments)
print(segment(2, [8,2,4,6]))
