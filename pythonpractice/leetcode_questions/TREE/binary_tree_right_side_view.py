class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.left.right.left = Node(7)
    return root

class Solution():
    def __init__(self, root) -> None:
        self.root = root

    def get_right_side_view(self):
        view = []
        max_height = 0
        def dfs(node, height):
            if not node:
                return
            nonlocal view, max_height
            height += 1
            if height > max_height:
                view.append(node.val)
                max_height += 1
            dfs(node.right, height)
            dfs(node.left, height)
        dfs(self.root, 0)
        return view

if __name__ == "__main__":
    solution = Solution(build_tree())
    print(solution.get_right_side_view())
