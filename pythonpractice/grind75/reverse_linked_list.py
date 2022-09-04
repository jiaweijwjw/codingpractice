# https://leetcode.com/problems/reverse-linked-list/

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def get_head(self):
        return self.head

    def insert_node(self, node):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
    

def print_ll(head):
    curr = head
    while curr:
        print(curr.val, end=" --> ")
        curr = curr.next
    print()

def build_ll(nums):
    ll = LinkedList()
    for num in nums:
        node = Node(num)
        ll.insert_node(node)
    head = ll.get_head()
    return head

def reverse_ll(head):
    new_head = None
    def reverse(prev, curr):
        nonlocal new_head
        next = curr.next
        curr.next = prev
        if not next:
            new_head = curr
            return
        reverse(curr, next)
    reverse(None, head)
    return new_head
    


if __name__ == "__main__":
    inputs = [[1,2,3,4,5],[1,2]]
    # outputs: [5,4,3,2,1], [2,1]
    for nums in inputs:
        head = build_ll(nums)
        print_ll(head)
        head = reverse_ll(head)
        print_ll(head)
