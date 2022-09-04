# https://leetcode.com/problems/linked-list-cycle/

class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

def build_ll_cycle():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next # 4 points to 2
    return head

def build_ll_no_cycle():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    return head

class Solution():
    def __init__(self) -> None:
        pass

    def has_cycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    solution = Solution()
    head_has_cycle = build_ll_cycle()
    head_no_cycle = build_ll_no_cycle()
    print(solution.has_cycle(head_has_cycle)) # True
    print(solution.has_cycle(head_no_cycle)) # False