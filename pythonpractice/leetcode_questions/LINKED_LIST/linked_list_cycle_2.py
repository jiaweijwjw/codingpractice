# https://leetcode.com/problems/linked-list-cycle-ii/
# https://leetcode.com/problems/linked-list-cycle-ii/discuss/1701128/C%2B%2BJavaPython-Slow-and-Fast-oror-Image-Explanation-oror-Beginner-Friendly

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add_node(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            prev = self.tail
            prev.next = node
            self.tail = node
        # curr = self.head
        # while curr.next: # while i can move next, 
        #     curr = curr.next # i will move next
        # # at this point, i will be at the last node in the linked list where next points to None
        # curr.next = node # we set it to point to this newly added node instead
        # self.tail = node

    def edit_next_node(self, node, next_node_index):
        if next_node_index == -1: 
            return
        pos = 0
        curr = self.head
        # curr will point at the node at the index pos, curr and pos will move together
        while pos < next_node_index:
            curr = curr.next
            pos += 1
        node.next = curr

    # for any distance travelled by the slow ptr, the fast ptr would have travelled twice as much
    # since we are using the slow and fast ptr algorithm, the fast ptr is guaranteed to meet the slow ptr if there is a cycle
    # they will meet when the slow ptr is in its first traversal in the cycle, while the fast pointer may have traverse the cycle many times
    # since we want to find the first node where the cycle begins, we set the distance travelled by the slow ptr to be (x + y)
    # whereby x is the distance from the start point to the first node where the cycle begins
    # and y is the distance from the first node where the cycle begins will the point that it will meet the fast ptr
    # since we know that the fast ptr is travelling twice as fast, it would have travelled as distance of 2(x + y)
    # as we have mentioned above, when the fast ptr and slow ptr meets, the fast ptr could have travelled a few times around the length of the cycle
    # the additional distance travelled by the fast ptr is equivalent to the number of times it has circled the cycle
    # hence we can derive the following formula: (x + y) = 2(x + y) - C
    # where C is the distance where fast ptr has traversed in the cycle
    # simplifying the formula, we get x = N*C - y
    
    def get_cycle_begin_node(self):
        if not self.head:
            return
        slow = fast = head = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # got cycle
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head # head would have moved to the first node of the cycle
        return None # no cycle

if __name__ == "__main__":
    inputs = [([3,2,0,-4],1),([1,2],0),([1],-1)]
    # return node at start of cycle
    # outputs: node at index 1, node at index 0, None
    for values, cycle_start_index in inputs:
        linked_list = LinkedList()
        for val in values:
            linked_list.add_node(Node(val))
        linked_list.edit_next_node(linked_list.get_tail(), cycle_start_index)
        first_node = linked_list.get_cycle_begin_node()
        print(first_node.val) if first_node else print(None)

