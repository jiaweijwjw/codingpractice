class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root=None) -> None:
        self.root = root
    
    def get_root(self):
        return self.root

    def find_LCA(self, root, val1, val2):
        path1 = self.find_path(root, val1, [])
        path2 = self.find_path(root, val2, [])
        if len(path1) == 0  or len(path2) == 0:
            return # not found
        else:
            # the following will not work for this example: [1,2,3] [1,2,3,4] becos only checks still 3 but all is the same
            for i in range(1, max(len(path1), len(path2))):
                if path1[i] != path2[i]: # can skip the root because sure is LCA
                    return path1[i-1]
                else:
                    return path1[min(len(path1), len(path2))-1]
    
    def find_path(self, node, val, path):
        if not node:
            return
        path.append(node)
        if node.val == val:
            return path
        else:
            left = self.find_path(node.left, val, path=path[:])
            right = self.find_path(node.right, val, path=path[:])
            if not left and not right:
                return
            elif left:
                return left
            elif right:
                return right
            else:
                return




binary_tree = BinaryTree()
# NOTE THAT DOING LIKE THIS IS DIFFERENT BECAUSE THIS FAKE ROOT IS EXTERNAL
# IF U TRY TO DO binary_tree.get_root(), IT WILL STILL BE NONE
# hence if we want to test like this, we must manually pass the root here into the function called.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(binary_tree.find_path(root, 7, []))
print(binary_tree.find_LCA(root, 4, 5).val)


