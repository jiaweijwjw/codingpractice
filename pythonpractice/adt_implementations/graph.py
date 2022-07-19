from collections import defaultdict, deque
# when the values in a dictionary are collections (lists, dicts, etc.) In this case, the value (an empty list or dict) 
# must be initialized the first time a given key is used. While this is relatively easy to do manually, the defaultdict 
# type automates and simplifies these kinds of operations.

# for interviews questions, we usually wont need to use an adjacency matrix or adjacency list
# we can just use a hash table of hash

edges = [(0,1), (1,2), (2,3), (3,4), (4,0), (4,5), (5,6)]

class Graph():
    def __init__(self, edges) -> None:
        self.graph = defaultdict(list) # hash table of lists
        self.edges = edges

    def build_graph(self):
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)

    def print_dfs_from_source(self, s):
        visited = set()
        dfs_order_list = []
        self.dfs_traversal(s, visited, dfs_order_list)
        print(dfs_order_list)

    def dfs_traversal(self, v, visited, dfs_order_list):
        if v not in visited:
            visited.add(v)
            dfs_order_list.append(v)
            for neighbour in self.graph[v]:
                self.dfs_traversal(neighbour, visited, dfs_order_list)
        

    def print_bfs_from_source(self, s):
        visited = set()
        bfs_order_list = []
        self.bfs_traversal(s, visited, bfs_order_list)
        print(bfs_order_list)

    def bfs_traversal(self, s, visited, bfs_order_list):
        q = deque()
        q.append(s)
        while q:
            v = q.popleft()
            if v not in visited:
                visited.add(v)
                bfs_order_list.append(v)
                for neighbour in self.graph[v]:
                    q.append(neighbour)
        

if __name__ == "__main__":
    graph = Graph(edges)
    graph.build_graph()
    graph.print_dfs_from_source(0)
    graph.print_bfs_from_source(0)
