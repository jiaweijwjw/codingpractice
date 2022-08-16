# https://leetcode.com/problems/same-tree/

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
    return root

def get_inorder(root): # left, root, right
    inorder_list = []
    def inorder_traversal(node):
        nonlocal inorder_list
        if not node:
            return
        inorder_traversal(node.left)
        inorder_list.append(node.val)
        inorder_traversal(node.right)
    inorder_traversal(root)
    return inorder_list

def get_preorder(root): # root, left, right
    preorder_list = []
    def preorder_traversal(node):
        nonlocal preorder_list
        if not node:
            return
        preorder_list.append(node.val)
        preorder_traversal(node.left)
        preorder_traversal(node.right)
    preorder_traversal(root)
    return preorder_list

def construct_tree(inorder, preorder): # root_index to track preorder list from left to right. start end to track inorder list subarrays
    preorder_index = 0
    def construct(start, end):
        if start > end:
            return
        nonlocal preorder_index
        root_val = preorder[preorder_index]
        preorder_index += 1
        root = Node(root_val)
        root_index = inorder.index(root_val)
        root.left = construct(start, root_index-1)
        root.right = construct(root_index+1, end)
        return root
    reconstructed_root = construct(0, len(inorder)-1)
    return reconstructed_root

def invert_tree(root):
    if not root:
        return
    temp_left = invert_tree(root.right)
    temp_right = invert_tree(root.left)
    root.left = temp_left
    root.right = temp_right
    return root

class Solution():
    def __init__(self) -> None:
        pass

    def is_same_tree(self, root1, root2) -> bool:
        if not root1 and not root2:
            return True # must return True not None
        elif (root1 and not root2) or (root2 and not root1):
            return False
        elif root1.val != root2.val:
            return False
        return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)


if __name__ == "__main__":
    solution = Solution()
    root = build_tree()
    inorder = get_inorder(root)
    preorder = get_preorder(root)
    print(inorder)
    clone_root = construct_tree(inorder, preorder)
    clone_inorder = get_inorder(clone_root)
    print(clone_inorder)
    inverted_root = invert_tree(root) # the original root is modified
    inverted_inorder = get_inorder(inverted_root)
    inverted_preorder = get_preorder(inverted_root)
    clone_inverted_root = construct_tree(inverted_inorder, inverted_preorder)
    root = invert_tree(root) # change root back
    print(solution.is_same_tree(root, clone_root))
    print(solution.is_same_tree(root, clone_inverted_root))