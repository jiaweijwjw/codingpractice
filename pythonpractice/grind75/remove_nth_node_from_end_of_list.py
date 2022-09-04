# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def append_node(self, node):
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def get_head(self):
        return self.head

def linked_list_builder(nums):
    linked_list = LinkedList()
    for num in nums:
        linked_list.append_node(Node(num))
    return linked_list.get_head()

def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end=" --> ")
        curr = curr.next
    print()
    
class Solution():
    def __init__(self) -> None:
        pass

    def remove_nth_node(self, head, n):
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next # no stitching done
        while fast.next:
            slow = slow.next
            fast = fast.next # pointing to last node
        slow.next = slow.next.next
        return head
        

if __name__ == "__main__":
    solution = Solution()
    inputs = [([1,2,3,4,5],2),([1],1),([1,2],1)]
    # outputs: [1,2,3,5], [], [1]
    for nums, n in inputs:
        head = linked_list_builder(nums)
        print_linked_list(head)
        head = solution.remove_nth_node(head, n)
        print_linked_list(head)