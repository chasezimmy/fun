"""
Find the sum of all left leaves in a given binary tree.

Example:

        5
       / \
      3   7
     / \  /
   .2  4 .6

sum: 8 (2+6)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def sum_of_leaves(root):
    sum_of_leaves.sum = 0
    def __(root, is_left=False):
        if not root: return
        if is_left and not root.left and not root.right: 
            sum_of_leaves.sum += root.val
        __(root.left, True)
        __(root.right)
    __(root)
    return sum_of_leaves.sum
    
root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)

print(sum_of_leaves(root))
