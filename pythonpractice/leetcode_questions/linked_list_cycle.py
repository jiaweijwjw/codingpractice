class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def add_node(self, node):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.next = node
    
    def get_node_at_index(self, index):
        if not self.head:
            return None
        else:
            curr_index = 0
            curr = self.head
            while(curr_index < index):
                curr_index += 1
                if not curr.next:
                    return None
                curr = curr.next
            return curr

    def edit_next_node(self, node, next_node):
        node.next = next_node

    def get_head(self):
        return self.head

    def print_linked_list(self):
        if not self.head:
            print("empty linkedlist")
            return None
        curr = self.head
        while curr:
            if curr.next:
                print(curr.val, end=" --> ")
            else:
                print(curr.val)
            curr = curr.next


class Solution():
    def __init__(self, head=None) -> None:
        self.head = head

    def has_cycle(self):
        if not self.head:
            return False
        slow, fast = self.head, self.head
        while fast and fast.next: # fast.next.next?
            slow = slow.next
            fast = fast.next.next
            if fast == slow: # why must this be after? if not first iteration will be true since both pointing to head
                return True
        return False


linkedlist = LinkedList()
for i in range(1, 5):
    linkedlist.add_node(Node(i))
linkedlist.print_linked_list()
linkedlist.edit_next_node(linkedlist.get_node_at_index(3), linkedlist.get_node_at_index(1))
# linkedlist.print_linked_list()
solution = Solution(linkedlist.get_head())
print(solution.has_cycle())