# Time:  O(n)
# Space: O(h)
#
# Invert a binary tree.
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# to
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#

# Time:  O(n)
# Space: O(w), w is the max number of the nodes of the levels.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
	def invert(self, root):
		if root is not None:
			root.left, root.right = self.invert(root.right), self.invert(root.left)

		self.inorder(root)

	def inorder(self, root):
		if root:
			self.inorder(root.left)
			print(root.val)
			self.inorder(root.right)



sol = Solution()
tree = Node(4)
tree.left = Node(2)
tree.left.left = Node(1)
tree.left.right = Node(3)
tree.right = Node(7)
tree.right.left = Node(6)
tree.right.right = Node(9)

invert = sol.invert(tree)
#sol.inorder(invert)