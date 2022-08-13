# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(20)
    root.left = Node(10)
    root.right = Node(50)
    root.left.left = Node(9)
    root.left.right = Node(15)
    root.right.right = Node(70)
    root.left.left.left = Node(7)
    root.left.right.left = Node(13)
    root.left.right.right = Node(18)
    root.right.right.left = Node(60)
    root.right.right.right = Node(90)
    return root

class BST():
    def __init__(self) -> None:
        pass

    def print_inorder(self, root):
        inorder_list = []
        def inorder_traversal(node):
            nonlocal inorder_list
            if not node:
                return
            inorder_traversal(node.left)
            inorder_list.append(node.val)
            inorder_traversal(node.right)
        inorder_traversal(root)
        print(inorder_list)

    def get_LCA(self, root, val1, val2): # assuming the values exist
        if not root:
            return
        if root.val == val1 or root.val == val2:
            return root
        elif (root.val > val1 and root.val < val2) or (root.val < val1 and root.val > val2):
            return root
        elif root.val > val1 and root.val > val2:
            return self.get_LCA(root.left, val1, val2)
        elif root.val < val1 and root.val < val2:
            return self.get_LCA(root.right, val1, val2)

if __name__ == "__main__":
    bst = BST()
    root = build_tree()
    bst.print_inorder(root)
    lca = bst.get_LCA(root, 10, 18)
    print(lca.val if lca else lca)