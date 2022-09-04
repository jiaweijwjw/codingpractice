# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# https://leetcode.com/problems/invert-binary-tree/

from collections import deque

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left= None
        self.right = None


def build_tree():
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.left.left = Node(55)
    root.right.left = Node(8)
    root.right.right = Node(32)
    root.right.right.left = Node(1)
    return root

class Tree():
    def __init__(self) -> None:
        pass

    # left root right
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

    # root left right
    def print_preorder(self, root):
        preorder_list = []
        def preorder_traversal(node):
            nonlocal preorder_list
            if not node:
                return
            preorder_list.append(node.val)
            preorder_traversal(node.left)
            preorder_traversal(node.right)
        preorder_traversal(root)
        print(preorder_list)

    # left right root
    def print_postorder(self, root):
        postorder_list = []
        def postorder_traversal(node):
            nonlocal postorder_list
            if not node:
                return
            postorder_traversal(node.left)
            postorder_traversal(node.right)
            postorder_list.append(node.val)
        postorder_traversal(root)
        print(postorder_list)
        

    def print_bfs_level_order(self, root):
        bfs_level_order_list = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                bfs_level_order_list.append(level)
        print(bfs_level_order_list)

    def get_max_height(self, node, height=1):
        if not node:
            return height-1 # since we added before we came in
        height = max(self.get_max_height(node.left, height+1), self.get_max_height(node.right, height+1))
        return height

    def invert(self, node):
        if not node:
            return
        temp_left = self.invert(node.right)
        temp_right = self.invert(node.left)
        node.right = temp_right
        node.left = temp_left
        return node



if __name__ == "__main__":
    tree = Tree()
    root = build_tree()
    tree.print_inorder(root)
    tree.print_preorder(root)
    tree.print_postorder(root)
    tree.print_bfs_level_order(root)
    print(tree.get_max_height(root))
    inverted_root = tree.invert(root)
    tree.print_bfs_level_order(inverted_root)
    tree.print_inorder(inverted_root)