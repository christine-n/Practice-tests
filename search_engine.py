class Trie_Node:
    def __init__(self):
        self.Arr = [False] * 26
        self.stop = False
        self.weight = 0

    def __str__(self):
        return str(self.Arr)


Root = Trie_Node()


def insert(s, weight):
    current = Root
    print('\n {}'.format(current))
    print('again')
    current.weight = max(weight, current.weight)
    for c in s:
        i = ord(c) - 97
        if not current.Arr[i]:
            current.Arr[i] = Trie_Node()
        current = current.Arr[i]
        current.weight = max(weight, current.weight)
    current.stop = True


def search_prefix(s):
    s = s.lower()
    current = Root
    for c in s:
        i = ord(c) - 97
        if not current.Arr[i]:
            return -1
        current = current.Arr[i]
    return current.weight


if __name__ == '__main__':
    """
        -- input --
        2 1
        hackerearth 10
        hackerrank 9
        hacker

        -- output ---
        10
    """
    n, m = map(int, input().split())

    for _ in range(n):
        s, w = input().split()
        w = int(w)
        insert(s, w)

    for _ in range(m):
        s = input()
        print(search_prefix(s))
