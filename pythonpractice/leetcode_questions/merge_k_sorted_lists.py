import heapq
import sys
sys.path.append("..")
# from adt_implementations import LinkedList, Node
from reverse_linked_list import LinkedList, Node

def print_from_head(head):
    if not head:
        print("empty linkedlist")
        return
    curr = head
    while curr:
        if curr.next:
            print(curr.val, end=" --> ")
        else:
            print(curr.val)
        curr = curr.next

lists = [[1,4,5],[1,3,4],[2,6]]
# lists = [[1,2,3]]
lists_of_linked_lists = []
for list in lists:
    new_linked_list = LinkedList()
    for item in list:
        new_linked_list.add_node(Node(item))
    lists_of_linked_lists.append(new_linked_list.get_head())

for linked_list in lists_of_linked_lists:
    print_from_head(linked_list)


class Solution():
    def __init__(self, k_lists) -> None:
        self.heap = []
        self.k_lists = k_lists

    def merge(self):
        head = Node(None)
        ptr = head
        # some edge cases for slightly faster performance
        if len(self.k_lists) == 0:
            return None
        elif len(self.k_lists) == 1:
            return self.k_lists[0]

        # add all to heap first
        for list in self.k_lists:
            curr = list
            while curr:
                heapq.heappush(self.heap, curr.val)
                curr = curr.next
        # when pop out from heap, will be sorted. by default is min heap
        while len(self.heap) > 0:
            ptr.next = Node(heapq.heappop(self.heap))
            ptr = ptr.next
        return head.next

solution = Solution(lists_of_linked_lists)
print_from_head(solution.merge())




