# we will try to implement a binary search tree (BST) here
# a binary search tree is whereby all nodes on the left subtree is less than the node and all nodes on the right subtree is greater than the node
# some common methods that we will do on a BST are: insert, delete, find
# the find method is the core method as the other methods will require it
# for example, to delete a node, we will first have to run find() on the BST
# likewise, to insert a node, we will first have to run find() to locate the position to insert the new node
# find_min and find_max is also a useful function
# for example, to find the successor of a node, we are actually calling find_min on the node's right subtree
# and likewise, to find the predecessor of a node, we are actually calling find_min on the node's left subtree
# some additional methods would also be: height_of_BST, ADD MORE?
# for deletion of a node, there are 3 cases: when the node has no child (leaf), has 1 child or has 2 children
# deletion of a leaf node is easy, just detach it from the parent
# deletion of a node with 1 child is also easy, just assign the child to the parent
# deletion of a ndoe with 2 child is more complicated. first, we have to change the node to the value of it's successor
# then, since deletion is carried out recursively, the remaining nodes will automatically be fixed also
# traversals of BST: 

import enum
class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class Child(enum.Enum):
    left = 0
    right = 1

class BST():
    def __init__(self, root=None) -> None:
        self.root = root

    def get_root(self):
        return self.root

    def insert_node(self, node):
        if not self.root:
            self.root = node # insert into empty BST
        else:
            self._insert_node(self.root, node)

    def _insert_node(self, node, node_to_insert):
        if node_to_insert.val > node.val: # right subtree
            if not node.right:
                node.right = node_to_insert
                return
            else:
                self._insert_node(node.right, node_to_insert)
        elif node_to_insert.val < node.val:
            if not node.left:
                node.left = node_to_insert
                return
            else:
                self._insert_node(node.left, node_to_insert)

    def find_val(self, val):
        if not self.root:
            return # empty BST
        else:
            return self._find_val(self.root, val)

    def _find_val(self, node, val_to_find):
        if node.val == val_to_find: # found
            return node
        if val_to_find > node.val:
            if node.right:
                return self._find_val(node.right, val_to_find)
            else:
                return
        elif val_to_find < node.val:
            if node.left:
                return self._find_val(node.left, val_to_find)
            else:
                return
        else:
            return # cant find val in BST

    # the magic is that we no need to parents, think of it as connecting 2 arrows into 1
    # this helps in both the finding part and the assigning part
    def delete_node(self, root, val):
        print(root.val)
        if not root:
            return root
        if val < root.val:
            root.left = self.delete_node(root.left, val)
        elif val > root.val:
            root.right = self.delete_node(root.right, val)
        else: # val == root.val
            if not root.right and not root.left: # 0 child
                root = None
            elif not root.left: # 1 child on the left
                root = root.right
            elif not root.right:
                root = root.left
            elif root.right and root.left: # 2 children
                successor = self.find_successor(root.right)
                root.val = successor.val
                root.right = self.delete_node(root.right, successor.val)
        return root


    def find_successor(self, node): # root of right subtree
        if not node.left:
            return node
        node = node.left
        return self.find_successor(node)

    def find_predecessor(self, node): # root of left subtree
        if not node.right:
            return node
        node = node.right
        return self.find_predecessor(node)

    def _find_parent(self, val, node):
        if not node: # empty BST
            return None, None
        if val == node.val: # no parent / root node
            return node, None
        elif val < node.val and node.left:
            if node.left.val == val:
                return node, Child.left
            else:
                return self.find_parent(val, node.left)
        elif val > node.val and node.right:
            if node.right.val == val:
                return node, Child.right
            else:
                return self.find_parent(val, node.right)
        else: # val not found
            return None, None

    def print_inorder(self):
        inorder_list = []
        if self.root:
            self.inorder_traversal(self.root, inorder_list)
        else:
            print("empty BST")
            return
        for i in range(len(inorder_list)):
            if i == len(inorder_list)-1:
                print(inorder_list[i])
            else:
                print(inorder_list[i], end= " --> ")
            
    def inorder_traversal(self, node, inorder_list):
        if node.left:
            self.inorder_traversal(node.left, inorder_list)
        inorder_list.append(node.val)
        if node.right:
            self.inorder_traversal(node.right, inorder_list)

    def preorder_traversal(self, node, preorder_list):
        pass

    def postorder_traversal(self, node, postorder_list):
        pass



bst = BST()
bst.insert_node(Node(8))
bst.insert_node(Node(3))
bst.insert_node(Node(11))
bst.insert_node(Node(10))
bst.insert_node(Node(5))
bst.insert_node(Node(1))
bst.insert_node(Node(6))
bst.insert_node(Node(4))
bst.print_inorder()
root = bst.get_root()
bst.delete_node(root, 3)
bst.print_inorder()