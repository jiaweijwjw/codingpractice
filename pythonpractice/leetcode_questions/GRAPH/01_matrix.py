import enum
from collections import deque

grid= [[0,0,0], # [[0,0,0]
       [0,1,0], #  [0,1,0]
       [1,1,1]] #  [1,2,1]]

class Dir(enum.Enum): # (c, r)
    right = 1, 0
    down = 0, 1
    left = -1 ,0
    up = 0, -1

# although this solution works, it will enter TLE error for very big cases
# because the general idea of this solution is that we find all the 1s and do BFS from that 1 as a source to find the nearest 0
# imagine we got a very big grid with only a single corner cell as 0, for each 1 to find that corner 0, it would take a long time
class Solution():
    def __init__(self, grid) -> None:
        self.grid = grid
        self.dist_matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # create a 0 matrix to store the ans

    def find_nearest_zero(self):
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] != 0:
                    self._bfs(r, c)
        return self.dist_matrix

    # since bfs is not recursive, we cannot pass dist as argument
    def _bfs(self, r, c):
        visited = set() # we set the visited here as we need to reset it for every bfs iteration
        q = deque()
        q.append(((c, r), -1)) # cell, dist
        while q:
            cell, dist = q.popleft()
            if cell not in visited:
                dist += 1
                if self.grid[cell[1]][cell[0]] == 0:
                    self.dist_matrix[r][c] = dist
                    break # no need search any further
                visited.add(cell)
                for dir in Dir:
                    neighbour = tuple(sum(coord) for coord in zip(cell, dir.value))
                    if neighbour not in visited and self._within_bounds(neighbour):
                        q.append((neighbour, dist))

    def _within_bounds(self, cell):
        c, r = cell[0], cell[1]
        if 0 <= r <= len(self.grid)-1 and 0 <= c <= len(self.grid[0])-1:
            return True
        else:
            return False

    

if __name__ == "__main__":
    solution = Solution(grid)
    print(solution.find_nearest_zero())
