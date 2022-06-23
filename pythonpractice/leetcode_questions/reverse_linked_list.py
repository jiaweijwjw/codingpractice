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
    
    def get_head(self):
        return self.head

    def print_linked_list(self):
        if not self.head:
            print("empty linkedlist")
            return
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

    def reverse_linkedlist(self):
        if not self.head:
            return None
        else:
            return self.reverse(None, self.head)

    def reverse(self, prev_node, node):
        next_node = node.next
        node.next = prev_node
        if not next_node:
            return node
        else:
            return self.reverse(node, next_node)

    def print_ans(self, node):
        if not node:
            print("empty linkedlist")
            return
        while node:
            if node.next:
                print(node.val, end=" --> ")
            else:
                print(node.val)
            node = node.next


linkedlist = LinkedList()
for i in range(1, 6):
    linkedlist.add_node(Node(i))
linkedlist.print_linked_list()
solution = Solution(linkedlist.get_head())
solution.print_ans(solution.reverse_linkedlist())
# reverse empty linked list
solution = Solution()
solution.print_ans(solution.reverse_linkedlist())