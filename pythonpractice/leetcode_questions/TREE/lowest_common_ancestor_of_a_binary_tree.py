class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)
    root.right.left = Node(0)
    root.right.right = Node(8)
    root.left.right.left = Node(7)
    root.left.right.right = Node(4)
    return root

class Solution():
    def __init__(self, root) -> None:
        self.root = root

    def find_LCA(self, node1, node2):
        return self._find_LCA(self.root, node1, node2)

    # for a node to be an LCA, it can node1 and node2 must either be the node itself or a descendant of this node
    # this means that either node1 or node2 can also be the LCA if the other node is it's descendent
    # as usual, we will enter the None node also and exit
    # if a root's value is same as that of node1 and node2, we can return this root too
    # why does this work? when reading the conditional check, if seems like this just means checking that node1 or node2 has been found
    # but notice that this can mean 2 things, either this root really means that we just found node1 or node2, and the LCA is further up
    # OR it can mean that this root which is node1 or node2 is the LCA and the other node2/node1 respectively is the descendent
    # this makes use of the property that either one of the node1 or node2 can also be the LCA if the other node is it's descendent
    # the recurse magic then happens after this. 
    # we call the function recursively on the left and right child of root and evaluate them
    # if both left and right child return a node, this root is the LCA
    # else, when we reverse the recursion call stack, we pass back the child which contains the node1 or 2 that was found
    def _find_LCA(self, root, node1, node2):
        if not root:
            return
        if root.val == node1.val or root.val == node2.val:
            return root
        left = self._find_LCA(root.left, node1, node2)
        right = self._find_LCA(root.right, node1, node2)
        if left and right:
            return root
        else:
            return left or right


if __name__ == "__main__":
    solution = Solution(build_tree())
    node1 = Node(10)
    node2 = Node(4)
    lca = solution.find_LCA(node1, node2)
    if lca:
        print(lca.val)