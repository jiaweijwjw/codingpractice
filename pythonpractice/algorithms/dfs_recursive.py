from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs_recursively(self, v, visited): # recursion is an implicit stack already
        visited.add(v)
        print(v, end=" -> ")
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_recursively(neighbour, visited)

    def dfs(self, s): # start doing DFS from the chosen source vertex
        visited = set() # cant use {} as it defaults to python dict
        self.dfs_recursively(s, visited)

graph = Graph()
edges = [(0,1), (0,2), (1,2), (2,0), (2,3), (3,3)]
for u, v in edges:
    graph.add_edge(u, v)
graph.dfs(2)