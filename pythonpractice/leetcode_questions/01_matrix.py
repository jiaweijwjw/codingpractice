import enum
from queue import Queue
from math import inf

matrix = [[0,0,0],
          [0,1,0],
          [1,1,1]]

class Dir(enum.Enum):
    up = 0, -1
    right = 1, 0
    down = 0, 1
    left = -1, 0

def solution(matrix):
    # dist_matrix = [[0]*len(matrix[0])]*len(matrix) # this kind of assignment will reuse the list for the remaining rows which will cause the other rows to be edited when u only edited one of the row
    dist_matrix = [[0]*len(matrix[0]) for i in range(len(matrix))]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] != 0:
                bfs(matrix, dist_matrix, (c, r))
                print()
    return dist_matrix

def dfs(matrix, dist_matrix, coord):
    q = [] # stack
    visited = set() # put visited here so every iteration of bfs will have a new visited
    min_dist = inf
    dist = -1 # first one dont count as a step
    q.append(coord)
    while q:
        print(q)
        curr = q.pop()
        print("curr:", curr)
        visited.add(curr)
        dist += 1
        if matrix[curr[1]][curr[0]] == 0:
            print(dist)
            visited.remove(curr)
            if dist < min_dist:
                min_dist = dist
            dist -= 1
            print(dist)
            continue
        for dir in Dir:
            neighbour = tuple(sum(i) for i in zip(curr, dir.value))
            if 0 <= neighbour[0] < len(matrix[0]) and 0 <= neighbour[1] < len(matrix) and neighbour not in visited:
                q.append(neighbour)
    dist_matrix[coord[1]][coord[0]] = min_dist
    print(dist_matrix[coord[1]][coord[0]])
    for row in dist_matrix:
        print(row)
    return

def bfs(matrix, dist_matrix, coord):
    q = Queue()
    visited = set() # put visited here so every iteration of bfs will have a new visited
    # first one dont count as a step, so start with -1
    q.put((coord, -1)) # the kind of question that need to store a state up till a certain node, need to pass value into child
    # if we are diong recursively, we usually pass in through function params. in this case, we store in the queue together with the coord
    while not q.empty():
        print(list(q.queue))
        curr, curr_dist = q.get()
        print("curr: ", curr)
        print("curr_dist: ", curr_dist)
        curr_dist += 1
        visited.add(curr)
        if matrix[curr[1]][curr[0]] == 0:
            dist_matrix[coord[1]][coord[0]] = curr_dist
            for row in dist_matrix:
                print(row)
            return
        for dir in Dir:
            neighbour = tuple(sum(i) for i in zip(curr, dir.value))
            if 0 <= neighbour[0] < len(matrix[0]) and 0 <= neighbour[1] < len(matrix) and neighbour not in visited:
                q.put((neighbour, curr_dist))

print(solution(matrix))

q = Queue()
a = ((1,2), 5)
q.put(a) 
q.put(((1,2), 5)) 
print(list(q.queue))
tup, dist = q.get()
print(tup, dist)