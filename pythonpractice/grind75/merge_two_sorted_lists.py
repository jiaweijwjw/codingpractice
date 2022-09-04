# https://leetcode.com/problems/merge-two-sorted-lists/

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
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

def create_ll(nums):
    ll = LinkedList()
    for num in nums:
        ll.add_node(Node(num))
    return ll.get_head()

def print_ll(head):
    curr = head
    while curr:
        if curr.next:
            print(curr.val, end=" -> ")
        else:
            print(curr.val)
        curr = curr.next

class Solution():
    def __init__(self) -> None:
        pass

    def merge_sorted_lists(self, head1, head2):
        if not head1 and not head2:
            return
        elif not head1:
            return head2
        elif not head2:
            return head1
        else:
            dummy = ptr = Node(None) # to maintain the start of the new merged linked list
            while head1 and head2:
                if head1.val < head2.val:
                    ptr.next = head1 # assign the next node that ptr is pointing to first
                    head1 = head1.next
                else:
                    ptr.next = head2
                    head2 = head2.next
                ptr = ptr.next # move ptr to the newly added node
            # attach the remaining nodes of the longer linked list, or None
            ptr.next = head1 or head2
            merged_head = dummy.next
            return merged_head





if __name__ == "__main__":
    solution = Solution()
    inputs = [([1,2,4],[1,3,4]),([],[]),([],[0])]
    for list1, list2 in inputs:
        head1 = create_ll(list1)
        head2 = create_ll(list2)
        print_ll(head1)
        print_ll(head2)
        merged_head = solution.merge_sorted_lists(head1, head2)
        if merged_head: print_ll(merged_head)
