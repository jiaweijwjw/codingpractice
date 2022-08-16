# https://leetcode.com/problems/validate-binary-search-tree/

from math import inf 

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

# we use this simple way to manually build our Trees
def build_tree(is_bst=False):
    if is_bst:
        root = Node(4)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.left.right = Node(3)
        return root
    else:
        root = Node(5)
        root.left = Node(4)
        root.right = Node(6)
        root.right.left = Node(3)
        root.right.right = Node(7)
        return root
    

# a tree is a binary search tree is all elements on the left are smaller and all elements on the right are larger
# the algorithm for validating is simple:
# we go through the entire tree recursively and return False anytime the rule above is broken
# if the entire tree has been traversed and the rule is not broken, then return False
class Tree():
    def __init__(self, root) -> None:
        self.root = root

    def is_bst(self) -> bool:
        return self._validate_recursively(self.root, -inf, inf)

    # think of it as both left and right subtrees have to return True then is valid
    def _validate_recursively(self, node, left_boundary, right_boundary):
        if not node:
            return True
        if not left_boundary < node.val < right_boundary:
            return False
        return (self._validate_recursively(node.left, left_boundary, node.val) and self._validate_recursively(node.right, node.val, right_boundary))
        
    # this one does not work because it only checks if the child on left is less and child on right is larger than a current node
    # but we have to account for the parent node as boundary too
    def _validate_recursively2(self, node):
        if not node:
            return True
        if node.left and node.left.val > node.val:
            return False
        if node.right and node.right.val < node.val:
            return False
        return self._validate_recursively(node.left) and self._validate_recursively(node.right)

        

if __name__ == "__main__":
    bst = Tree(build_tree(is_bst=True))
    print(bst.is_bst())
    not_bst = Tree(build_tree(is_bst=False))
    print(not_bst.is_bst())