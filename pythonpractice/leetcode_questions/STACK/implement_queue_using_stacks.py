class MyQueue:

    def __init__(self):
        self.enqueue_stack = [] # push into queue
        self.dequeue_stack = [] # pop first element from queue

    def push(self, x: int) -> None:
        self.enqueue_stack.append(x)

    def pop(self) -> int:
        if self.dequeue_stack: # dequeue stack not empty
            return self.dequeue_stack.pop()
        elif not self.enqueue_stack: # dequeue stack is empty and enqueue stack is also empty, nothing to move over
            return None
        else: # move from enqueue stack to dequeue stack
            while(self.enqueue_stack):
                item = self.enqueue_stack.pop()
                if len(self.enqueue_stack) == 0:
                    return item
                else:
                    self.dequeue_stack.append(item)

    def peek(self) -> int:
        if self.dequeue_stack:
            return self.dequeue_stack[len(self.dequeue_stack)-1] # no need to pop it off
        elif not self.enqueue_stack:
            return None
        else:
            while(self.enqueue_stack):
                item = self.enqueue_stack.pop()
                self.dequeue_stack.append(item)
            return self.dequeue_stack[len(self.dequeue_stack)-1]

    def empty(self) -> bool:
        if not self.enqueue_stack and not self.dequeue_stack:
            return True
        else:
            return False

    def size(self) -> int:
        return len(self.enqueue_stack) + len(self.dequeue_stack)
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())
print(obj.pop())
obj.push(4)
obj.push(5)
print(obj.size())
print(obj.empty())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.size())
print(obj.empty())