class TreeNode:
    def __init__(self, key=0, left=None, right=None):
        self.val = key
        self.left = left
        self.right = right

    def insertBinaryTree(self, root, key):
        if root is None:
            root = TreeNode(key)
            return
        else:
            if root.val == key:
                return root
            elif key < root.val:
                root.left = self.insertBinaryTree(root.left, key)
            else:
                root.right = self.insertBinaryTree(root.right, key)
        return root

    def maxDepthBinaryTree(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.maxDepthBinaryTree(root.left),
                           self.maxDepthBinaryTree(root.right))

    def printTree(self, root, arr):
        #
        if root is None:
            return 'None'
        else:
            if root.left:
                print(self.printTree(root.left, arr.append(root.left)))
            else:
                print(self.printTree(root.right, arr.append(root.right)))
        return arr

if __name__ == '__main__':
    tree = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(tree[0])
    for i in range(1, len(tree)):
        root = root.insertBinaryTree(root, i)
    # print(root)
    # print(root.maxDepthBinaryTree(root))
    arr = []
    root.printTree(root, [])
