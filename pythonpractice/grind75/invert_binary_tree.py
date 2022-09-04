# https://leetcode.com/problems/invert-binary-tree/

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def __init__(self) -> None:
        pass

    def invert_binary_tree(self, root):
        if not root:
            return root
        temp_left = self.invert_binary_tree(root.right)
        temp_right = self.invert_binary_tree(root.left)
        root.left = temp_left
        root.right = temp_right
        return root

def create_binary_tree():
    root = Node(4)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(9)
    return root

def print_tree_inorder(root):
    inorder_list = []
    def inorder_traversal(node):
        if not node:
            return
        nonlocal inorder_list
        inorder_traversal(node.left)
        inorder_list.append(node.val)
        inorder_traversal(node.right)
    inorder_traversal(root)
    print(inorder_list)

if __name__ == "__main__":
    solution = Solution()
    root = create_binary_tree()
    print_tree_inorder(root)
    solution.invert_binary_tree(root)
    print_tree_inorder(root)
    # outputs: 