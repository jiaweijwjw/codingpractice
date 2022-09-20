# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def create_bst():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.left.left.left = Node(1)
    return root

class Solution():
    def __init__(self) -> None:
        pass

    def get_kth_smallest_element(self, root, k):
        el = None
        count = 0
        # inorder traversal. left, right, root
        def traverse(root):
            nonlocal el, count
            if not root:
                return
            traverse(root.left)
            count += 1
            if count == k:
                el = root.val
                return # no need to continue finding
            traverse(root.right)
        traverse(root)
        return el # if k exceeds the number of elements in the bst, el will not be found and hence will return el = None

if __name__ == "__main__":
    solution = Solution()
    root = create_bst()
    k = 3
    print(solution.get_kth_smallest_element(root, k))