import queue
from collections import defaultdict


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self, x, y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(s):
        print(s)


t = int(input())
# t = 2
for i in range(t):
    n, m = [int(value) for value in input().split()]
    print(n, m)
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    # s = int(input())
    s = 6
    graph.find_all_distances(s - 1)

print('sour')

x = defaultdict()
print(x['i'])