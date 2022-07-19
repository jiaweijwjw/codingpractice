from collections import deque

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(5)
    root.left = Node(4)
    root.right = Node(6)
    root.right.left = Node(3)
    root.right.right = Node(7)
    return root


class BinaryTree():
    def __init__(self, root) -> None:
        self.root = root

    # inorder, preorder and postorder traversals are all depth first search traversals
    # inorder is left, root, right
    # preorder is root, left, right
    # postorder is left, right, root
    def print_inorder(self):
        inorder_list = []
        self._inorder_traversal(self.root, inorder_list)
        print("inorder recursive")
        print(inorder_list)
        print()

    def _inorder_traversal(self, node, inorder_list):
        if not node:
            return
        self._inorder_traversal(node.left, inorder_list)
        inorder_list.append(node.val)
        self._inorder_traversal(node.right, inorder_list)

    def print_preorder(self):
        preorder_list = []
        self._preoder_traversal(self.root, preorder_list)
        print("preorder recursive")
        print(preorder_list)
        print()
        
    def _preoder_traversal(self, node, preorder_list):
        if not node:
            return
        preorder_list.append(node.val)
        self._preoder_traversal(node.left, preorder_list)
        self._preoder_traversal(node.right, preorder_list)

    def print_postorder(self):
        postorder_list = []
        self._postorder_traversal(self.root, postorder_list)
        print("postorder recursive")
        print(postorder_list)
        print()

    def _postorder_traversal(self, node, postorder_list):
        if not node:
            return
        self._postorder_traversal(node.left, postorder_list)
        self._postorder_traversal(node.right, postorder_list)
        postorder_list.append(node.val)

    def print_bfs_order(self):
        bfs_list = []
        self._bfs_traversal(self.root, bfs_list)
        print("bfs order")
        print(bfs_list)
        print()

    def _bfs_traversal(self, root, bfs_list):
        q = deque() # queue
        q.append(root)
        while q:
            node = q.popleft()
            if not node:
                continue
            bfs_list.append(node.val)
            q.append(node.left)
            q.append(node.right)

    def print_inorder_iterative(self):
        inorder_list = []
        self._inorder_traversal_iterative(self.root, inorder_list)
        print("inorder iterative")
        print(inorder_list)
        print()

    # to visualize the tree and this iterative approach, it would be easier to include the None nodes when drawing the tree
    # this algorithm would be easier to understand with a pseudocode:
    # since it is a dfs approach, we would require a stack instead of a queue in bfs
    # the curr variable acts like a pointer to the node which we are visiting. remember to draw out the entire tree with the None nodes!
    # while True meaning an infinite loop, we will go through each node by modifying the node which curr is pointing to
    # for every subtree / tree, move curr to the left most node
    # for every node that we pass by, add it to the stack
    # in this specific example, we will first start from 5, then push it onto stack, then on to 4 and push it into stack
    # we stop when we ENTER the None node
    # in this left and downward traversal, when a None is seen, we pop a node from the stack
    # popping this node would be the parent of the None node (or the root node if we think in terms of root, left, right as parent, left child, right child)
    # then, we restart this entire traversing left and dowanwards algorithm on the right child of this node that was popped
    # in this case, when we enter 4.right, it is None already
    # hence, as we mentioned earlier, once we see a None, we pop from the stack
    # this time, 5 will be popped from the stack
    # then we append 5 to the list
    # and likewise, after popping, we restart the entire algorithm on the right side of the node that was popped
    # we go to 6, then since its not None, we push 6 into stack and move to 3. and since 3 is also not None, we push into stack and move to None
    # likewise, once None is since, we pop from stack
    # up till this point, you should be able to understand the algorithm
    def _inorder_traversal_iterative(self, root, inorder_list):
        s = deque() # stack
        curr = root
        while True:
            if curr:
                s.append(curr)
                curr = curr.left
            else: # curr is None
                if s:
                    node = s.pop()
                    inorder_list.append(node.val)
                    curr = node.right
                else:
                    break

    def print_preorder_iterative(self):
        preorder_list = []
        self._preorder_traversal_iterative(self.root, preorder_list)
        print("preorder iterative")
        print(preorder_list)
        print()

    # preorder iteratively is not the same as inorder, completely different algorithm
    # the general idea is:
    # push right then push left of curr into the stack
    # then append curr into the preorder list
    # then we want to pop the stack until we reach not None
    # to do this we use the same algorithm, but we check if curr is None at the start. if it is None, then we pop from the stack again
    # when not None node is popped from stack, redo the entire algorithm again
    # until stack is empty
    def _preorder_traversal_iterative(self, root, preorder_list):
        s = deque()
        curr = root
        while True:
            if not curr:
                if s:
                    curr = s.pop()
                else:
                    break
            else:
                s.append(curr.right)
                s.append(curr.left)
                preorder_list.append(curr.val)
                if s:
                    curr = s.pop()
                else:
                    break 

    # def print_postorder_iterative(self):
    #     postorder_list = []
    #     self._postorder_traversal_iterative(self.root, postorder_list)
    #     print(postorder_list)


    # def _postorder_traversal_iterative(self, root, postorder_list):
    #     s = deque()
    #     curr = root
    #     while True:
    #         if curr:
    #             s.append(curr)
    #             curr = curr.left
    #         else: # curr is None
    #             while s:
    #                 top = s[-1]
    #                 if not top.right:
    #                     node = s.pop()
    #                     postorder_list.append(node.val)
    #                     if s:
    #                         next_top = s[-1]
    #                         if node == next_top.right:
    #                             pass
    #                         else:
    #                             pass
    #                     else:
    #                         break



if __name__ == "__main__":
    tree = BinaryTree(build_tree())
    tree.print_inorder()
    tree.print_preorder()
    tree.print_postorder()
    tree.print_bfs_order()
    tree.print_inorder_iterative()
    tree.print_preorder_iterative()
    # tree.print_postorder_iterative()
