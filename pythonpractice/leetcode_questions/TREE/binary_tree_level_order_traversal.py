from collections import deque

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    return root

class Solution():
    def __init__(self, root) -> None:
        self.root = root

    def get_level_order(self):
        level_order_list = []
        self._bfs_level_order(self.root, level_order_list)
        return level_order_list

    def _bfs_level_order(self, root, level_order_list):
        if not self.root:
            return
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
            if len(level) > 0:
                level_order_list.append(level)
                



if __name__ == "__main__":
    solution = Solution(build_tree())
    print(solution.get_level_order())