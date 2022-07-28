class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    return root

class BinaryTree():
    def __init__(self, root) -> None:
        self.root = root

    def print_preorder(self):
        preorder_list = []
        self._preorder_traversal(self.root, preorder_list)
        print(preorder_list)

    def _preorder_traversal(self, node, preorder_list):
        if not node:
            return
        self._preorder_traversal(node.left, preorder_list)
        preorder_list.append(node.val)
        self._preorder_traversal(node.right, preorder_list)

    def get_max_height(self):
        if not self.root:
            return 0
        return self._find_max_height(self.root, 1)

    def _find_max_height(self, node, height):
        if not node:
            return height-1 # since already added when we came in this node
        height = max(self._find_max_height(node.left, height+1), self._find_max_height(node.right, height+1))
        return height

    def invert_binary_tree(self):
        self._invert(self.root)

    def _invert(self, node):
        if not node: # this line is important to handle the case whereby a node only has one child and the other child is None
            return node
        if not node.left and not node.right: # leaf node, no need swap the child
            return node
        # none leaf node, swap the child
        temp_left = self._invert(node.right)
        temp_right = self._invert(node.left)
        node.left = temp_left
        node.right = temp_right
        return node

    def find_LCA(self, node1, node2):
        return self._find_LCA(self.root, node1, node2)

    def _find_LCA(self, root, node1, node2):
        if not root:
            return
        if root.val == node1.val or root.val == node2.val:
            return root
        left = self._find_LCA(root.left, node1, node2)
        right = self._find_LCA(root.right, node1, node2)
        if left and right:
            return root
        else:
            return left or right

if __name__ == "__main__":
    tree = BinaryTree(build_tree())
    print(tree.get_max_height())
    tree.print_preorder()
    tree.invert_binary_tree()
    tree.print_preorder()
    lca = tree.find_LCA(Node(3), Node(7))
    if lca:
        print(lca.val)