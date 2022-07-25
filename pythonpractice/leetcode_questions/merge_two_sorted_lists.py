# import sys
# import pathlib
# # import os
# from pprint import pprint
# # import pathlib
# # pprint(pathlib.Path().parent.parent.resolve())
# # pprint(os.path.abspath(os.getcwd().parent))
# directory = pathlib.Path() / "adt_implementations"
# sys.path.append(directory.parent.parent.resolve())
# pprint(sys.path)
# from adt_implementations.linked_list import LinkedList, Node
import sys
sys.path.append("..")
from adt_implementations.linked_list import LinkedList, Node

def create_linked_list(my_list):
    linked_list = LinkedList()
    for el in my_list:
        linked_list.add_node(Node(el))
    return linked_list.get_head()

class Solution():
    def __init__(self, list1, list2) -> None:
        self.list1_head = list1 # points to the head of the linked list
        self.list2_head = list2

    def merge_two_linked_lists(self):
        ptr = dummy = Node(None)
        list1, list2 = self.list1_head, self.list2_head
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next
        ptr.next = list1 or list2 # for the linked list that is longer, if both same length, then it will point to None
        return dummy.next # dummy.next would be the head of the linked list


    def print_merged(self, head):
        curr = head
        while curr:
            if curr.next:
                print(curr.val, end=" --> ")
            else:
                print(curr.val)
            curr = curr.next


if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]
    solution = Solution(create_linked_list(list1), create_linked_list(list2))
    head = solution.merge_two_linked_lists()
    solution.print_merged(head)