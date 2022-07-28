class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def build_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    return head

class Solution():
    def __init__(self, linked_list_head) -> None:
        self.linked_list_head = linked_list_head

    def get_head(self):
        return self.linked_list_head

    def print_linked_list(self, head):
        curr = head
        while curr:
            if curr.next:
                print(curr.val, end=" --> ")
            else:
                print(curr.val)
            curr = curr.next

    def remove_nth_node_from_end(self, n):
        fast = slow = head = self.linked_list_head
        for _ in range(n): # assume that n is smaller than the length of the linked list
            fast = fast.next
        # if not fast:
        #     return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        

if __name__ == "__main__":
    solution = Solution(build_linked_list())
    solution.print_linked_list(solution.get_head())
    solution.remove_nth_node_from_end(2)
    solution.print_linked_list(solution.get_head())