"""
Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, 
and satisfies the constraint that the key in the left child must be 
less than or equal to the root and the key in the right child must be 
greater than or equal to the root.
"""

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

