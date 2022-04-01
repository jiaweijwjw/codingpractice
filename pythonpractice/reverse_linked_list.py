class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, node):
        node.next = self.head # current head will be 'pushed' in
        self.head = node

    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def print_linked_list(self):
        node = self.head
        while node.next:
            print(node.val, end=" ")
            node = node.next
        print(node.val)


linked_list = LinkedList()
list_of_nodes = [ListNode(val) for val in range(1, 10)]
for node in list_of_nodes: 
    linked_list.add(node)

linked_list.print_linked_list() 
linked_list.reverse()
linked_list.print_linked_list()