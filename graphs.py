from typing import List

def findMinHeightTrees(n: int, edges: List[List[int]]) -> List[int]:
    # Input: n = 4, edges = [[1,0],[1,2],[1,3]]
    # Output: [1]
    graph = [set() for _ in range(n)]

    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    print(graph)

    leaves = [x for x in range(n) if len(graph[x]) <= 1]
    prev_leaves = leaves
    while leaves:
        new_leaves = []
        for leaf in leaves:
            if not graph[leaf]:
                return leaves
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
        prev_leaves, leaves = leaves, new_leaves

    return prev_leaves


if __name__ == '__main__':
    print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))