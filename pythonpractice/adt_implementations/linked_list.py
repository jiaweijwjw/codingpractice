# some list ADT operations include: get(i), remove(i), insert(i, v), find(v)

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_LL(self):
        curr = self.head
        while(curr):
            print(curr.val, " --> ", end="")
            curr = curr.next

    def insert_head(self, node):
        curr = self.head
        node.next = curr
        self.head = node

    def find(self, val):
        """returns the index of a searched value if there exists a node with this value"""
        itr = self.head
        index = 0
        while(itr):
            if itr.val == val:
                return index
            else:
                itr = itr.next
                index += 1
        return None


linked_list = LinkedList()
list_of_nodes = [Node(num**2) for num in range(1, 7)]
for node in list_of_nodes:
    linked_list.insert_head(node)

linked_list.print_LL()
print(linked_list.find(4))
