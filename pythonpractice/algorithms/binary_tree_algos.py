from collections import deque
class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(7)
    return root


class BinaryTree():
    def __init__(self, root) -> None:
        self.root = root

    # inorder, preorder and postorder traversals are all depth first search traversals
    # inorder is left, root, right
    # preorder is root, left, right
    # postorder is left, right, root
    def print_inorder(self):
        inorder_list = []
        self._inorder_traversal(self.root, inorder_list)
        print(inorder_list)

    def _inorder_traversal(self, node, inorder_list):
        if not node:
            return
        self._inorder_traversal(node.left, inorder_list)
        inorder_list.append(node.val)
        self._inorder_traversal(node.right, inorder_list)

    def print_preorder(self):
        preorder_list = []
        self._preoder_traversal(self.root, preorder_list)
        print(preorder_list)
        
    def _preoder_traversal(self, node, preorder_list):
        if not node:
            return
        preorder_list.append(node.val)
        self._preoder_traversal(node.left, preorder_list)
        self._preoder_traversal(node.right, preorder_list)

    def print_postorder(self):
        postorder_list = []
        self._postorder_traversal(self.root, postorder_list)
        print(postorder_list)

    def _postorder_traversal(self, node, postorder_list):
        if not node:
            return
        self._postorder_traversal(node.left, postorder_list)
        self._postorder_traversal(node.right, postorder_list)
        postorder_list.append(node.val)

    def print_bfs_order(self):
        bfs_list = []
        self._bfs_traversal(self.root, bfs_list)
        print(bfs_list)

    def _bfs_traversal(self, root, bfs_list):
        q = deque() # queue
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                continue
            bfs_list.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def print_inorder_iterative(self):
        inorder_list = []
        self._inorder_traversal_iterative(self.root, inorder_list)
        print(inorder_list)

    def _inorder_traversal_iterative(self, root, inorder_list):
        s = deque() # stack
        curr = root
        while True:
            if curr:
                s.append(curr)
                curr = curr.left
            else: # curr is None
                if s:
                    curr = s.pop()
                    inorder_list.append(curr.val)
                    s.append(curr.right)
                else:
                    break
            
            





if __name__ == "__main__":
    tree = BinaryTree(build_tree())
    tree.print_inorder()
    tree.print_preorder()
    tree.print_postorder()
    tree.print_bfs_order()
    tree.print_inorder_iterative()
