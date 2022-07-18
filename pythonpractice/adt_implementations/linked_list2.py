# some list ADT operations include: get(i), remove(i), insert(i, v), find(v)

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def get_head(self):
        return self.head

    def print_LL(self):
        if not (self.head and self.tail):
            print("Please insert some nodes before printing the linked list.")
            return
        # print(f"length of linked list is {self.len}")
        # print(f"current head is {self.head.val}")
        # print(f"current tail is {self.tail.val}")
        # print("linked list: ", end="")
        curr = self.head
        while(curr):
            if curr.next: # not last node
                print(curr.val, " --> ", end="")
            else:
                print(curr.val)
            curr = curr.next

    def insert(self, node, pos): # insert(v, i) / insert(i, v)
        """inserts a node at a specified index
            4 scenarios: at head, when empty, after tail, anywhere else (including at tail)"""
        if pos > self.len or pos < 0:
            print("Unsuccessful insert at position out of range.")
            return
        if pos == 0: # insert at head, insert_head function accounts for empty linked list case already
            self.insert_head(node)
        elif pos == self.len: # after tail
            curr_tail = self.tail
            curr_tail.next = node
            self.tail = node
            self.len += 1
        else: # not at head
            itr = self.head
            while(pos-1): # iterate throught the linked list pos-1 times. the -1 is because we want to be 1 index before the actual insertion position
                # we have to set the prev.next to point to this new node but in a singly linked list, there is not previous pointer
                temp = itr.next
                itr = temp
                pos -= 1
            node.next = itr.next
            itr.next = node
            self.len += 1
            
    def insert_head(self, node):
        self.len += 1
        curr = self.head
        node.next = curr
        self.head = node
        if curr is None: # first item in linked list
            self.tail = node

    def remove(self, pos):
        """removes a node at a specified index"""
        if pos >= self.len or pos < 0:
            print("Unsuccessful remove at position out of range.")
            return
        if pos == 0:
            self.remove_head()
        elif pos == self.len-1:
            self.remove_tail()
        else:
            itr = self.head
            while(pos-1):
                temp = itr.next
                itr = temp.next
                pos -= 1
            next = itr.next
            itr.next = next.next
            next.next = None
            del next
            self.len -= 1
            
    def remove_head(self):
        curr_head = self.head
        self.head = curr_head.next
        del curr_head
        self.len -= 1

    def remove_tail(self): # has to iterate through the entire linked list to remove tail, O(n)
        itr = self.head
        while(itr.next.next): # next node is not the tail
            temp = itr.next
            itr = temp.next
        tail = self.tail
        self.tail = itr
        itr.next = None
        del tail
        self.len -= 1

    def find_index_of_val(self, val): # search(v) / find(v)
        """returns the index of a searched value if there exists a node with this value"""
        itr = self.head
        index = 0
        while(itr):
            if itr.val == val:
                return index
            else:
                itr = itr.next
                index += 1
        return None

    def get_val_at_index(self, index): # get(i)
        """returns the value of a node at a given index within range"""
        if index >= self.len:
            return
        else:
            itr = self.head
            while(index):
                temp = itr.next
                itr = temp
            return itr.val


# linked_list = LinkedList()
# list_of_nodes = [Node(num**2) for num in range(1, 7)]
# for node in list_of_nodes:
#     linked_list.insert_head(node)


# linked_list.print_LL()
# linked_list.insert(Node(999), -1)
# linked_list.print_LL()
# linked_list.remove_tail()
# linked_list.print_LL()
# linked_list.remove_head()
# linked_list.print_LL()
# linked_list.remove(-1)
# linked_list.remove(1)
# linked_list.print_LL()