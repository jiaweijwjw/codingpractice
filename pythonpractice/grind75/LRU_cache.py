# https://leetcode.com/problems/lru-cache/

# this is more of a design problem rather than an algorithms problem
# since we need to get and put in O(1), we can use a hashmap / dictionary
# there is only 1 problem that we need to solve which is how do we maintain the ordering i.e. which is least recently used?
# whenever we get or put an item into the cache, it will become the most recently used
# to solve this problem, we first know that we have to use a dictionary to maintain the key-value pairs
# however, instead of directly storing the value as the actual value, we will store the value as a node holding the key-value pair
# why do we need to store the key again? this will be explained below
# next, we solve the problem of maintaining the most and least recently used elements by storing them in a doubly linked list
# why does a doubly linked list work?
# note the constraint is that get and put must be in O(1)
# everytime we get(), we need to move and element to the right most (most recently used)
# everytime we put(), we also need to consider the case where the least recently used (most left) item must be evicted
# if an array was used, we have to account for the shifting of the remaining elements which is O(n) time complexity
# a double ended queue may solve the put() problem, but not the get() problem as get() can be any element in the middle
# now that we have settle on using a doubly linked list, realise that we have to delete the key from the dictionary when the LRU element is evicted
# hence we have to store this key in the doubly linked list node, so that we can properly delete it from the dictionary instead of searching

class Node():
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:

    # LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity # the max capacity that cache can hold
        self.lru = Node() # left bound dummy
        self.mru = Node() # right bound dummy
        self.lru.right = self.mru
        self.mru.left = self.lru

    # int get(int key) Return the value of the key if the key exists, otherwise return -1.
    def get(self, key: int) -> int:
        # if the key exists, we have to make it the mru
        node =  self.cache.get(key, None)
        if not node:
            return -1    
        else: # key exists, move to mru
            self.update_most_recent(node)
        return node.val
        
    # void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
    # If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if not node: # key does not exists
            new_node = Node(key, value)
            if len(self.cache) == self.capacity: # cache is full, need to evict lru
                least_recent = self.lru.right
                self.remove_node(least_recent)
                del self.cache[least_recent.key] # dont forget to remove the key of the evicted node
            self.set_as_most_recent(new_node)
            self.cache[key] = new_node
        else: # update the value since key already exists
            node.val = value
            self.update_most_recent(node) # dont forget to update

    # helper functions
    def update_most_recent(self, node=None):
        self.remove_node(node)
        self.set_as_most_recent(node)

    def set_as_most_recent(self, node):
        most_recent = self.mru.left
        most_recent.right = node
        self.mru.left = node
        node.left = most_recent
        node.right = self.mru

    def remove_node(self, node): # connects the left and right of this node
        left = node.left
        right = node.right
        left.right = right
        right.left = left




if __name__ == "__main__":
    # Your LRUCache object will be instantiated and called as such:
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    print(lRUCache.get(1))
    lRUCache.put(3, 3)
    print(lRUCache.get(2))
    lRUCache.put(4, 4)
    print(lRUCache.get(1)) 
    print(lRUCache.get(3)) 
    print(lRUCache.get(4))