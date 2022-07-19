from collections import deque

nums = [5,2,6,3,4,1,7]

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BST():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, node) -> bool:
        if not self.root:
            self.root = node
            return True
        return self._insert(self.root, node)

    def _insert(self, root, node) -> bool:
        if node.val > root.val:
            if root.right:
                return self._insert(root.right, node)
            else:
                root.right = node
                return True
        elif node.val < root.val:
            if root.left:
                return self._insert(root.left, node)
            else:
                root.left = node
                return True
        else:
            return False

    def delete(self, val):
        return self._delete(self.root, val)

    def _delete(self, node, val):
        if not node: # val cant be found
            return node
        if val > node.val:
            node.right = self._delete(node.right, val)
        elif val < node.val:
            node.left = self._delete(node.left, val)
        else: # found val, val == node.val
            if not node.left and not node.right:
                node = None # return at the end
            # for single child, cannot check together. we also use the not condition because the both child case will also cause the 1 child case to be true
            elif not node.left:
                node = node.right
            elif not node.right:
                node = node.left
            else: # has 2 child
                predecessor = self.find_predecessor(node.left)
                node.val = predecessor.val # copy the value
                node.left = self._delete(node.left, predecessor.val)
        return node

    def find_predecessor(self, root):
        curr = root
        while curr.right:
            curr = curr.right
        return curr
    
    def find_successor(self, root):
        curr = root
        while curr.left:
            curr = curr.left
        return curr
            
    def print_bfs(self):
        bfs_list = []
        self._bfs_traversal(self.root, bfs_list)
        print(bfs_list)

    def _bfs_traversal(self, root, bfs_list):
        q = deque()
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
        print(inorder_list)

    def _inorder_traversal_iterative(self, root, inorder_list):
        s = deque()
        curr = root
        while True:
            if curr:
                s.append(curr)
                curr = curr.left
            else: # go all the way left into None
                if s:
                    node = s.pop()
                    inorder_list.append(node.val)
                    curr = node.right
                else:
                    break



 
if __name__ == "__main__":
    bst = BST()
    for num in nums:
        bst.insert(Node(num))
    bst.print_inorder_iterative()
    bst.delete(6)
    bst.print_inorder_iterative()
