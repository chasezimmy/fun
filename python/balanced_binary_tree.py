class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 


def is_balanced(root):
    def __(root):
        if not root:
            return 0
        
        h1 = __(root.left)
        h2 = __(root.right)

        if h1 == -1 or h2 == -2 \
            or abs(h1 - h2) > 1:
            return -1

        if h1 > h2: return h1 + 1
        return h2 + 1
    return __(root) > 0


root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.right.right = Node(4)
root.right.right.right = Node(5)
#            1
#          /   \
#        2       3
#                  \
#                    4
#                      \
#                        5

print(is_balanced(root))