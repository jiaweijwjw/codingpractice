from collections import defaultdict
from queue import PriorityQueue

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)


    def bfs(self, s): # start doing BFS from the chosen source vertex
        queue = PriorityQueue()
        visited = set()
        queue.put(s)
        print(queue.empty())
        while not queue.empty():
            v = queue.get()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbour in self.graph[v]:
                    if neighbour not in visited:
                        queue.put(neighbour)
        print(visited)
            

graph = Graph()
edges = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,2)]
for u, v in edges:
    graph.add_edge(u, v)
graph.bfs(3)