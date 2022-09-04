# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def create_bst():
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.left.left = Node(0)
    root.left.right = Node(4)
    root.right.left = Node(7)
    root.right.right = Node(9)
    root.left.right.left = Node(3)
    root.left.right.right = Node(5)
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

class Solution():
    def __init__(self) -> None:
        pass

    def find_lca(self, root, node1, node2):
        if not root:
            return
        if root.val == node1.val or root.val == node2.val:
            return root
        elif node1.val < root.val < node2.val or node2.val < root.val < node1.val:
            return root
        elif root.val < node1.val and root.val < node2.val:
            return self.find_lca(root.right, node1, node2)
        elif root.val > node1.val and root.val > node2.val:
            return self.find_lca(root.left, node1, node2)


if __name__ == "__main__":
    solution = Solution()
    existent_pairs = [(2,9),(2,5),(0,5)]
    # outputs: 6, 2, 2
    root = create_bst()
    print_tree_inorder(root)
    for node1, node2 in existent_pairs:
        lca = solution.find_lca(root, Node(node1), Node(node2))
        if lca: print(lca.val)