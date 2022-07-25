from collections import deque
from random import randrange

adjList = [[2,4],[1,3],[2,4],[1,3]]
# adjList itself is already a graph representation

class Node():
    def __init__(self, val, neighbours=None) -> None:
        self.val = val
        self.neighbours = neighbours if neighbours is not None else []

# the graph representation that we create here will use an adjlist too, or we can do the usual way of using defaultdict
# but the adjList here will be actual Nodes instead of just values
# we will be creating an undirected graph here
# the logic in creating the graph here, can be used in the solution to clone the graph
class Graph():
    def __init__(self, adjList) -> None:
        self.graph = [None]*len(adjList) # this graph will store a list of all the nodes/vertex of the graph
        self.adjList = adjList
        self._create_graph()

    def _create_graph(self):
        for i in range(len(self.adjList)):
            v = self.graph[i] if self.graph[i] else Node(i+1) # if vertex not in list of vertices yet, create the vertex
            neighbours_val = self.adjList[i]
            for neighbour_val in neighbours_val:
                u = self.graph[neighbour_val-1] if self.graph[neighbour_val-1] else Node(neighbour_val)
                if v not in u.neighbours: u.neighbours.append(v)
                if u not in v.neighbours: v.neighbours.append(u)
                self.graph[neighbour_val-1] = u
            self.graph[i] = v

    def get_random_graph_vertex(self):
        v = self.graph[randrange(len(self.graph))]
        print(v.val)
        return v

    def print_graph_dfs(self):
        dfs_list = []
        visited = set()
        def _dfs_traversal(vertex):
            nonlocal dfs_list
            if vertex not in visited:
                visited.add(vertex)
                dfs_list.append(vertex.val)
                for neighbour in vertex.neighbours:
                    _dfs_traversal(neighbour)
        source = self.get_random_graph_vertex()
        print(f"source: {source.val}")
        _dfs_traversal(source)
        print(dfs_list)
    
class Solution():
    def __init__(self, source) -> None:
        self.source = source
        self.graph_clone = {} # if we use list there is alot of conditions to check because we cant know the size of the list at first
        self.source_clone = None

    # this question is a little complicated so let us walk through the steps and explain some of the variables and data structures used
    # firstly, what is graph clone? it is a dict with its key being the original node and the value being the new node
    # what this does it that it allows use to keep track of which nodes have been cloned
    # what it means is that if an original node can be found as the key in the graph_clone dict, the new node has been cloned and is the value
    # at any time, the size of the dict is the number of nodes that we have added to this graph
    # the bfs traversal of the original graph is nothing new
    # as usual, we require a visited set and a queue for bfs
    # note that the bfs traversal is just to traverse the original graph and no cloned nodes are pushed into the queue
    # the magic of cloning actually happens when we visit a node in the original graph
    # if u are unsure about how normal bfs traversal is done, take a look at my other questions which uses original bfs
    # now look at this line: new_node = self.graph_clone[node] if node in self.graph_clone else Node(node.val)
    # what this does is that if the node already exists in the graph_clone dict, it is already cloned,
    # so we do not want to reclone it aka calling Node() class constructor
    # instead, we just retrieve / take it out from the dict. this is done by calling graph_clone[original_node]. recall that key is original node and value is the new cloned node
    # why would we need to retrieve a cloned node? this would happen when we want to append a new neighbour to this new cloned node
    # because when we cloned it, the neighbours property of the cloned node is still empty, and we would only add to it while we traverse the original graph
    # the same logic applies to the new_neighbour_node. if the neighbour has already been cloned, we just retrieve it from the dict
    # once we have both the new_node and the new_neighbour_node, we just need to check if they are in each others' neighbour property
    # this is because we are creating an undirected graph meaning both nodes will store each other as a neighbour
    # after we are done adding the new_node and new_neighbour_node as each others' neighbour, we put them back into the dict
    # at the end, we return a clone of the original node by fetching the value in the dict with the original source node as key
    def clone_graph_bfs(self):
        if not self.source: # if empty graph, no node was passed in
            return self.source
        visited = set()
        q = deque()
        q.append(self.source)
        while q:
            node = q.popleft()
            if node not in visited:
                new_node = self.graph_clone[node] if node in self.graph_clone else Node(node.val)
                visited.add(node)
                for neighbour in node.neighbours:
                    new_neighbour_node = self.graph_clone[neighbour] if neighbour in self.graph_clone else Node(neighbour.val)
                    if new_neighbour_node not in new_node.neighbours: new_node.neighbours.append(new_neighbour_node)
                    if new_node not in new_neighbour_node.neighbours: new_neighbour_node.neighbours.append(new_node)
                    q.append(neighbour)
                    self.graph_clone[neighbour] = new_neighbour_node
                self.graph_clone[node] = new_node
        self.source_clone = self.graph_clone[self.source]
    
    def get_source_clone(self):
        return self.source_clone

    def get_random_graph_vertex(self):
        v = self.graph_clone[randrange(len(self.graph_clone))]
        print(v.val)
        return v



if __name__ == "__main__":
    graph = Graph(adjList)
    solution = Solution(graph.get_random_graph_vertex())
    solution.clone_graph_bfs()