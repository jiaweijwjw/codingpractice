class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_bst():
    root = Node(3)
    root.left = Node(1)
    root.right = Node(4)
    root.left.right = Node(2)
    return root

class Solution():
    def __init__(self, root, k) -> None:
        self.root = root
        self.k = k

    # the solution is actually just doing inorder traversal of a binary tree
    # slight modifications to the original inorder traversal is done
    # the recursive function is called using a return keyword. this allows us to cut short the resursion if the value is already found
    def get_kth_smallest_element(self):
        curr = 0
        element = None
        def _inorder_traversal(node, k):
            nonlocal curr, element
            if not node:
                return
            print(node.val)
            res = _inorder_traversal(node.left, k)
            if res:
                return
            curr += 1
            if curr == k:
                element = node.val
                return True
            return _inorder_traversal(node.right, k)
        _inorder_traversal(self.root, self.k)
        return element



if __name__ == "__main__":
    k = 1
    solution = Solution(build_bst(), k)
    print(solution.get_kth_smallest_element())
    