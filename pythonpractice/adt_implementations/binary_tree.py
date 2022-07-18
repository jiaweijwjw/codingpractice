# https://leetcode.com/problems/validate-binary-search-tree/discuss/786520/General-Tree-Traversal-Problems-interview-Prep

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

# to create normal binary tree, just do manually adding to a root node
# see below for example
# the following example will create a tree that looks like this:
#               1
#       2               3
#  4      5

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)