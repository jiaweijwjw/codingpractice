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
        self.max_height = 0

    def get_root(self):
        return self.root
    
    def get_max_height(self):
        return self.max_height

    def find_max_height(self, root, height):
        if not root:
            return height
        height = max(self.find_max_height(root.left, height+1), self.find_max_height(root.right, height+1))
        return height

    # from smallest to largest left to right to largest to smallest left to right and vice versa
    def invert_tree(self, root):
        if not root:
            return root
        if not root.right and not root.left:
            return root
        temp_left = self.invert_tree(root.right)
        temp_right = self.invert_tree(root.left)
        root.left = temp_left
        root.right = temp_right
        return root

    # if 2 nodes are siblings, return the first common parent
    # by definition of LCA, if one node is a parent of the other node, the LCA is the parent node
    def find_LCA2(self, root, val1, val2):
        if not root:
            return None
        if root.val == val1 or root.val == val2:
            return root
        if val1 < root.val:
            node1 = self.find_LCA(root.left, val1, val2)
        elif val1 > root.val:
            node1 = self.find_LCA(root.right, val1, val2)
        if val2 < root.val:
            node2 = self.find_LCA(root.left, val1, val2)
        elif val2 > root.val:
            node2 = self.find_LCA(root.right, val1, val2)
        if node1 and node2:
            return root
        elif node1 and not node2:
            return node1
        elif node2 and not node1:
            return node2
        else:
            return None

    def find_LCA(self, root, val1, val2):
        if not root:
            return
        if root.val == val1 or root.val == val2:
            return root
        # if both the val are on the same subtree, break the problem down further
        if val1 < root.val and val2 < root.val:
            return self.find_LCA(root.left, val1, val2)
        elif val1 > root.val and val2 > root.val:
            return self.find_LCA(root.right, val1, val2)
        # if they are splitting at any point, then this will be the LCA
        # the general idea of finding LCA is actually very simple, we just find the point where they start to split
        # however, my implementation also accounts for whether the 2 nodes can even be found, although the leetcode question doesnt require
        elif val1 < root.val and val2 > root.val or val1 > root.val and val2 < root.val:
            if val1 < root.val:
                node1 = self.find_LCA(root.left, val1, val2)
                node2 = self.find_LCA(root.right, val1, val2)
            elif val1 > root.val:
                node1 = self.find_LCA(root.right, val1, val2)
                node2 = self.find_LCA(root.left, val1, val2)
            if node1 and node2: # both vals can be found
                return root
            # the following conditions is needed to further check splits which will confirm be taken but will reach None for the other value
            elif not node1:
                return node2
            elif not node2:
                return node1
            else:
                return
        return root # if none of the cases, maybe BST only has 1 item
            

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
        # we return the root/node as it is part of our recursion
        if not root:
            return root
        if val < root.val:
            root.left = self.delete_node(root.left, val)
        elif val > root.val:
            root.right = self.delete_node(root.right, val)
        else: # val == root.val
            if not root.right and not root.left: # 0 child
                root = None
            elif not root.left: # 1 child on the right
                root = root.right
            elif not root.right: # 1 child on the left
                root = root.left
            elif root.right and root.left: # 2 children
                successor = self.find_successor(root.right)
                root.val = successor.val
                root.right = self.delete_node(root.right, successor.val)
                # we can either set the predecessor or the successor to replace the node to be deleted
                # predecessor = self.find_predecessor(root.left)
                # root.val = predecessor.val
                # root.left = self.delete_node(root.left, predecessor.val)
        # the following return root is one way to do recursion
        # think of it as we enter the left or right child,
        # but if nothing happens, we have to pass it back to the parent to set it back
        # hence we have to put the root.right = delete_node() assignment
        # if something happens (the root is to be deleted), the root value will be changed here and returned back to the parent
        # for example, when the current node has 0 child and it is the node to be deleted, we set this node(root) to None
        # then when it is returned to the parent, it will be set as None
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
root = bst.get_root()
print(bst.find_max_height(root, 0))
bst.invert_tree(root)
bst.print_inorder()
bst.invert_tree(root)
bst.print_inorder()
print(bst.find_LCA(root, 11, 10).val)