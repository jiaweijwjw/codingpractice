import enum
from queue import Queue

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

class Dir(enum.Enum):
    up = 0, -1 # dont need to put brackets here, also no need brackets
    right = 1, 0 # each of this is an enum
    down = 0, 1
    left = -1, 0

def solution(grid):
    num_of_islands = 0
    visited = set()
    for x in range(len(grid[0])): # cols
        for y in range(len(grid)): # rows
            if (x, y) not in visited and grid[y][x] == "1":
                bfs(grid, x, y, visited) # each bfs algo will cover one island
                num_of_islands += 1
    return num_of_islands

# visited will be marked here, so that in the main solution function, it will be skipped
def bfs(grid, x, y, visited):
    q = Queue()
    q.put((x, y)) # remember that x is columns and y is rows
    while not q.empty():
        print(list(q.queue))
        curr_pos = q.get()
        print(curr_pos)
        if curr_pos in visited:
            continue # move on to the next item in the queue
        else: # not yet visited
            visited.add(curr_pos) # careful dont reuse x, y
            for dir in Dir:
                neighbour = tuple(sum(coord) for coord in zip(curr_pos, dir.value))
                if (0 <= neighbour[0] < len(grid[0])) and (0 <= neighbour[1] < len(grid)) and (neighbour not in visited) and (grid[neighbour[1]][neighbour[0]] == "1"): # not out of grid
                    q.put(neighbour)

def solution2(grid):
    num_of_islands = 0
    visited = set()
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if (x, y) not in visited and grid[y][x] == "1":
                dfs(grid, x, y, visited)
                print(visited)
                num_of_islands += 1
    return num_of_islands

def dfs(grid, x, y, visited):
    visited.add((x, y))
    print((x, y))
    for dir in Dir:
        neighbour = tuple(sum(coord) for coord in zip((x, y), dir.value))
        # when accessing grids, make sure to check for boundaries before the other conditions
        if 0 <= neighbour[0] < len(grid[0]) and 0 <= neighbour[1] < len(grid) and grid[neighbour[1]][neighbour[0]] == "1" and neighbour not in visited:
            dfs(grid, neighbour[0], neighbour[1], visited)

print(solution2(grid))
