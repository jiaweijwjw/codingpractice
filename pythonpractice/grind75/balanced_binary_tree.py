# https://leetcode.com/problems/balanced-binary-tree/
class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def create_balanced_tree():
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    return root

def create_unbalanced_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(3)
    root.left.left.left = Node(4)
    root.left.left.right = Node(4)
    return root

class Solution():
    def __init__(self) -> None:
        pass

    def is_balanced_tree(self, root):
        is_balanced = True
        def traverse_tree(node, height):
            if not node:
                return height-1
            nonlocal is_balanced
            left_height = traverse_tree(node.left, height+1)
            right_height = traverse_tree(node.right, height+1)
            if abs(left_height-right_height) > 1:
                is_balanced = False
            return max(left_height, right_height)
        traverse_tree(root, height=1)
        return is_balanced


if __name__ == "__main__":
    solution = Solution()
    balanced_root = create_balanced_tree()
    unbalanced_root = create_unbalanced_tree()
    print(solution.is_balanced_tree(balanced_root))
    print(solution.is_balanced_tree(unbalanced_root))