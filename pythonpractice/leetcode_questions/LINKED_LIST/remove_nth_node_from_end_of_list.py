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
        # use dummy if want do stitching for all cases
        # exit early for during fast ptr incrementation if want to account for n > linked list length
        # use slow.next = fast does not work why?

        # slow = fast = dummy = Node(None)
        # dummy.next = head
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast: # because largest n is only length of the linked list for this question
            return head.next # no stitching done
        while fast.next:
            slow = slow.next
            fast = fast.next # pointing to last node
        # slow.next = fast # this doesnt work since we stop fast and the last node. this wont work if the gap between slow and fast is only 1
        slow.next = slow.next.next
        return head
        

if __name__ == "__main__":
    solution = Solution(build_linked_list())
    solution.print_linked_list(solution.get_head())
    solution.remove_nth_node_from_end(2)
    solution.print_linked_list(solution.get_head())