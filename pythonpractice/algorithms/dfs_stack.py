from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s):
        visited = set()
        stack = [] # append and pop
        stack.append(s)
        while len(stack):
            v = stack.pop()
            if v not in visited:
                print(v)
                visited.add(v)
                for neighbour in self.graph[v]:
                    if neighbour not in visited:
                        stack.append(neighbour)





edges = [(1,0), (0,2), (2,1), (0,3), (1,4)]
graph = Graph()
for u, v in edges:
    graph.add_edge(u, v)
graph.dfs(0)