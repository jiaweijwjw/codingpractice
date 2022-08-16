class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_bst():
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)
    root.right.right.left = Node(13)
    # 1,3,4,6,7,8,10,13,14
    return root

class Solution():
    def __init__(self, root) -> None:
        self.root = root

    # the solution is actually just doing inorder traversal of a binary tree
    # slight modifications to the original inorder traversal is done
    # the recursive function is called using a return keyword. this allows us to cut short the resursion if the value is already found
    def get_kth_smallest_element(self, k):
        curr = 0
        element = None
        def _inorder_traversal(node, k):
            nonlocal curr, element
            if not node:
                return
            res = _inorder_traversal(node.left, k)
            if res:
                return
            curr += 1
            if curr == k:
                element = node.val
                return True
            return _inorder_traversal(node.right, k)
        _inorder_traversal(self.root, k)
        return element


    def get_kth_largest_element(self, k):
        count = 0
        element = None
        def reverse_inorder_traversal(node, k):
            if not node:
                return
            nonlocal count, element
            reverse_inorder_traversal(node.right, k) # change this to left and it is the kth smallest element
            count += 1
            if count == k:
                element = node.val
                return
            reverse_inorder_traversal(node.left, k)
        reverse_inorder_traversal(self.root, k)
        return element



if __name__ == "__main__":
    solution = Solution(build_bst())
    print(solution.get_kth_smallest_element(k=3))
    print(solution.get_kth_largest_element(k=2))
    