# import sys
# sys.path.append("..")
# use this to import this linked list and node class into other files for testing purposes

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def get_head(self):
        return self.head

    def add_node(self, node):
        """used for adding nodes to create the linked list"""
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def insert_head(self, node):
        """also does the same think as adding nodes to the linked list but inserts through the head"""
        node.next = self.head
        self.head = node
        
    def reverse_linked_list(self):
        if not self.head:
            return self.head
        else:
            self._reverse(None, self.head)

    def _reverse(self, prev_node, curr_node):
        next_node = curr_node.next
        curr_node.next = prev_node
        if not next_node:
            self.head = curr_node
        else:
            self._reverse(curr_node, next_node)

    def get_node_at_index(self, index):
        """returns the node object at a specific given index, if the node is not found, None is returned.
            for simplicity's sake, assume that there is no cycle"""
        if not self.head:
            return
        else:
            curr_index = 0
            curr = self.head
            while curr_index < index:
                if not curr:
                    return
                curr = curr.next
                curr_index += 1
            return curr

    def edit_next_node(self, node, next_node):
        """points a node to another node. next node can be None to truncate the linked list"""
        if node == None:
            return
        node.next = next_node

    def has_cycle(self):
        if not self.head:
            return
        slow = fast = self.head
        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def print_linked_list(self, has_cycle=False):
        if has_cycle:
            checked = set()
            curr = self.head
            while curr:
                if curr.next:
                    print(curr.val, end=" --> ")
                else:
                    print(curr.val)
                if curr in checked:
                    checked.add(curr)
                    break
                checked.add(curr)
                curr = curr.next
            print()
        else: # normal printing
            curr = self.head
            while curr:
                if curr.next:
                    print(curr.val, end=" --> ")
                else:
                    print(curr.val)
                curr = curr.next
            print()

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_node(Node(1))
    linked_list.add_node(Node(2))
    linked_list.insert_head(Node(10))
    linked_list.insert_head(Node(9))
    linked_list.print_linked_list()
    linked_list.edit_next_node(linked_list.get_node_at_index(2), linked_list.get_node_at_index(0))
    linked_list.print_linked_list(True)
    print(linked_list.has_cycle())