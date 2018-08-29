# Lowest common ancestor

# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def lca(self, root, n1, n2):
        """ O(N) time complexity  """

        if root is None:
            return None

        if root.val == n1.val or root.val == n2.val:
            return root

        left = self.lca(root.left, n1, n2)
        right = self.lca(root.right, n1, n2)

        if left is not None and right is not None:
            return root

        if left is None and right is None:
            return None

        return left if left is not None else right;


def main():
    sol = Solution()

    tree = Node(3)
    tree.left = Node(6)
    tree.left.left = Node(2)
    tree.left.right = Node(11)
    tree.left.right.left = Node(9)
    tree.left.right.right = Node(5)
    tree.right = Node(8)
    tree.right.right = Node(13)
    tree.right.right.left = Node(7)

    
    print(sol.lca(tree, Node(2), Node(11)).val) # 2, 11, lca = 6    
    print(sol.lca(tree, Node(8), Node(7)).val) # 8, 7, lca = 8
    print(sol.lca(tree, Node(8), Node(11)).val) # 8, 11, lca = 3


if __name__=='__main__':
    main()
