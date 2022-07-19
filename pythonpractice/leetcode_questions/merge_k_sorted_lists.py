from heapq import heappush, heappop
import sys
sys.path.append("..")
from adt_implementations.linked_list import LinkedList, Node

# init some input
lists = [[1,4,5],[1,3,4],[2,6]] # output: [1,1,2,3,4,4,5,6]
list_of_linked_lists = []
for list in lists:
    linked_list = LinkedList()
    for item in list:
        linked_list.add_node(Node(item))
    list_of_linked_lists.append(linked_list)
    linked_list.print_linked_list()

class Solution():
    def __init__(self) -> None:
        self.heap = []

    def merge(self, list_of_linked_lists): # returns the first node in the ans linked list
        ptr = dummy_head = Node(None)
        # some edge cases to exit early
        if len(list_of_linked_lists) == 0:
            return None
        elif len(list_of_linked_lists) == 1:
            return list_of_linked_lists[0]
        
        for list in list_of_linked_lists:
            curr = list.get_head()
            while curr:
                heappush(self.heap, curr.val)
                curr = curr.next
        while self.heap:
            ptr.next = Node(heappop(self.heap))
            ptr = ptr.next
        return dummy_head.next
            

if __name__ == "__main__":
    solution = Solution()
    ans = LinkedList()
    head = solution.merge(list_of_linked_lists)
    ans.add_node(head)
    ans.print_linked_list()
