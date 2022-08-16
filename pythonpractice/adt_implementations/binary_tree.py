# https://leetcode.com/problems/validate-binary-search-tree/discuss/786520/General-Tree-Traversal-Problems-interview-Prep

# to create normal binary tree, just do manually adding to a root node
# see below for example
# the following example will create a tree that looks like this:
#                8
#             /    \
#           50     77
#          /  \      \
#        1     9     10 
#                   /
#                  33

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(8)
    root.left = Node(50)
    root.right = Node(77)
    root.left.left = Node(1)
    root.left.right = Node(9)
    root.right.right = Node(10)
    root.right.right.left = Node(33)
    return root

class BinaryTree():
    def __init__(self) -> None:
        pass

    # from the preorder / post order list, we iterate from left to right or right to left to constantly keep track of the root
    # the inorder list will give us the left and right subtree of the current root
    # use indexes to access the arrays. splicing takes O(N)

    def construct_tree(self, inorder, preorder): # root_index to track preorder list from left to right. start end to track inorder list subarrays
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

    def construct_tree2(self, inorder, postorder):
        postorder_index = len(postorder)-1
        def construct(start, end):
            if start > end:
                return
            nonlocal postorder_index
            root_val = postorder[postorder_index]
            postorder_index -= 1
            root = Node(root_val)
            root_index = inorder.index(root_val)
            root.right = construct(root_index+1, end) # Note that here we will have to do right first before left. reverse inorder
            root.left = construct(start, root_index-1)
            return root
        reconstructed_root = construct(0, len(inorder)-1)
        return reconstructed_root

    def get_inorder(self, root): # left, root, right
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

    def get_preorder(self, root): # root, left, right
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

    def get_postorder(self, root): # left, right, root
        postorder_list = []
        def postorder_traversal(node):
            nonlocal postorder_list
            if not node:
                return
            postorder_traversal(node.left)
            postorder_traversal(node.right)
            postorder_list.append(node.val)
        postorder_traversal(root)
        return postorder_list


if __name__ == "__main__":
    root = build_tree()
    binary_tree = BinaryTree()
    inorder = binary_tree.get_inorder(root)
    preorder = binary_tree.get_preorder(root)
    postorder = binary_tree.get_postorder(root)
    print(inorder)
    print(preorder)
    print(postorder)
    print()
    reconstructed_root = binary_tree.construct_tree(inorder, preorder)
    reconstructed_inorder = binary_tree.get_inorder(reconstructed_root)
    reconstructed_preorder = binary_tree.get_preorder(reconstructed_root)
    print(reconstructed_inorder)
    print(reconstructed_preorder)
    print()
    reconstructed_root = binary_tree.construct_tree2(inorder, postorder)
    reconstructed_inorder = binary_tree.get_inorder(reconstructed_root)
    reconstructed_postorder = binary_tree.get_postorder(reconstructed_root)
    print(reconstructed_inorder)
    print(reconstructed_postorder)




