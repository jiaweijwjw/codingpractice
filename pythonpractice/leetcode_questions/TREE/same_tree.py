
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
    root.right.left = Node(5)
    root.right.right = Node(6)
    return root

def build_tree2():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.right = Node(4)
    return root

class Solution():
    def __init__(self, tree1, tree2) -> None:
        self.root_tree1 = tree1
        self.root_tree2 = tree2

    def is_same_tree(self):
        return self._dfs_traverse(self.root_tree1, self.root_tree2)

    def _dfs_traverse(self, node1, node2):
        if not node1 and not node2:
            return True # MUST return true, if not it will just return None
        elif not node1 or not node2:
            return False
        elif node1.val != node2.val:
            return False
            # use AND operator not OR because we only want to return True if both is True
        return self._dfs_traverse(node1.left, node2.left) and self._dfs_traverse(node1.right, node2.right)


if __name__ == "__main__":
    solution = Solution(build_tree(), build_tree())
    print(solution.is_same_tree())
    solution2 = Solution(build_tree(), build_tree2())
    print(solution2.is_same_tree())