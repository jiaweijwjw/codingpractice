class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree1():
    root = Node(1)
    root.left = Node(3)
    root.right = Node(2)
    root.left.left = Node(5)
    return root

def build_tree2():
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    root.left.right = Node(4)
    root.right.right = Node(7)
    return root

class Solution():
    def __init__(self) -> None:
        pass

    def merge_two_binary_trees(self, root1, root2):
        merged_root = None
        if not root1 and not root2:
            return merged_root
        elif not root1: # only tree2 continues
            merged_root = Node(root2.val)
            merged_root.left = self.merge_two_binary_trees(None, root2.left)
            merged_root.right = self.merge_two_binary_trees(None, root2.right)        
        elif not root2: # only tree1 continues
            merged_root = Node(root1.val)
            merged_root.left = self.merge_two_binary_trees(root1.left, None)
            merged_root.right = self.merge_two_binary_trees(root1.right, None)    
        else: # both continues
            merged_root = Node(root1.val + root2.val)
            merged_root.left = self.merge_two_binary_trees(root1.left, root2.left)
            merged_root.right = self.merge_two_binary_trees(root1.right, root2.right)        
        return merged_root

    def print_tree_inorder(self, root):
        inorder_list = []
        def traverse_inorder(node):
            nonlocal inorder_list
            if not node:
                return
            traverse_inorder(node.left)
            inorder_list.append(node.val)
            traverse_inorder(node.right)
        traverse_inorder(root)
        print(inorder_list)

if __name__ == "__main__":
    solution = Solution()
    root1 = build_tree1()
    root2 = build_tree2()
    merged_root = solution.merge_two_binary_trees(root1, root2)
    solution.print_tree_inorder(merged_root)