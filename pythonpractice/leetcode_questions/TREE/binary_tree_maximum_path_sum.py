from collections import deque
from math import inf

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(-10)
    root.left = Node(9)
    root.left.left = Node(-5)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    return root

def build_tree2():
    root = Node(1)
    root.left = Node(-2)
    root.right = Node(-3)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(-2)
    root.left.left.left = Node(-1)
    return root

class Solution():
    def __init__(self, root) -> None:
        self.root = root

    # instead of using a self.sum variable, we try a different way of doing, using python inner functions
    # this way, we can also hide the inner function like a private class, but we can also encapsulate the sum variable to only be accessible
    # in this function. other class methods will not be able to access the sum variable
    def find_maximum_path_sum(self):
        sum = -inf # we have to set as -inf because there are negative numbers too
        def recurse_down(node):
            nonlocal sum # the variable sum from the outer function
            # instead of returning when reaching a leaf node, we enter the None node and return 0. just another way of doing it
            if not node:
                return 0
            left_sum = recurse_down(node.left)
            right_sum = recurse_down(node.right)
            # only updating of the sum variable includes node.val+left_sum+right_sum
            # DONT forget to add in the sum variable in the comparison to COMPARE and UPDATE with the previous sum value also
            sum = max(sum, node.val, node.val+left_sum, node.val+right_sum, node.val+left_sum+right_sum)
            # the return value should not include the both paths as it will split up the path, we have to choose EITHER left or right or dont add
            return max(node.val, node.val+left_sum, node.val+right_sum)
        recurse_down(self.root)
        return sum



    def find_maximum_path_sum2(self):
        return self._recurse_down2(self.root)

    # this solution is incorrect as it doesnt consider the fact that a path cannot split into 2
    # considering the fact that if we have a parent node that needs to connect with their child node,
    # if the child node connects its own left and right child, the path actualyl splits into 2
    def _recurse_down2(self, node):
        if not node.left and not node.right: # no children
            return node.val
        # we use NOT to check for the one other child if not the 2 child condition will be true also
        elif not node.left: # 1 child on the right
            right_sum = self._recurse_down(node.right)
            return max(node.val, right_sum, node.val+right_sum)
        elif not node.right: # 1 child on the left
            left_sum = self._recurse_down(node.left)
            return max(node.val, left_sum, node.val+left_sum)
        else: # 2 child
            right_sum = self._recurse_down(node.right)
            left_sum = self._recurse_down(node.left)
            return max(node.val, node.val+right_sum, node.val+left_sum, right_sum, left_sum, node.val+right_sum+left_sum)

    def print_bfs_order(self):
        bfs_order_list = []
        self._bfs_traversal(self.root, bfs_order_list)
        print(bfs_order_list)

    def _bfs_traversal(self, root, bfs_order_list):
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                bfs_order_list.append(node.val)
                q.append(node.left)
                q.append(node.right)

if __name__ == "__main__":
    solution = Solution(build_tree())
    solution.print_bfs_order()
    print(solution.find_maximum_path_sum())