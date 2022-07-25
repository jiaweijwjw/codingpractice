from queue import Queue
# this questions has 2 solutions
# either using 1 queue whereby we rotate
# or we use 2 queues where by we just alternate the queues to push into
# however in both cases, either push or pop will be O(n)
# however for the 2 queues one, top() also O(n), and also 2 queues are used.
# even though stores the same num of elements as one queue will always be empty

# this will be the one queue implementation as the 2 queue one is not difficult to visualize
class MyStack:

    def __init__(self):
        self.q = Queue() # use deque instead

    def push(self, x: int) -> None:
        self.q.put(x)
        for i in range(self.q.qsize()-1): # leave the last element out which is our newly pushed item
            item = self.q.get()
            self.q.put(item)

    def pop(self) -> int:
        if self.q.empty():
            return None
        else:
            return self.q.get()

    def top(self) -> int:
        if self.q.empty():
            return None
        else:
            return self.q.queue[0]

    def empty(self) -> bool:
        return self.q.empty()

    def size(self) -> int:
        return self.q.qsize()

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop()) # 3
print(obj.pop()) # 2
print(obj.top()) # 1
obj.push(4)
obj.push(5)
print(obj.empty()) # False
print(obj.pop()) # 5
print(obj.pop()) # 4
print(obj.pop()) # 1
print(obj.pop()) # None
print(obj.empty()) # True
print(obj.top()) # None
