import enum
from collections import deque

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

class Dir(enum.Enum): # (x, y) or (c, r)
    right = 1, 0
    down = 0, 1
    left = -1, 0
    up = 0, -1

class Solution():
    def __init__(self, grid) -> None:
        self.grid = grid

    def get_number_of_islands(self) -> int:
        num_of_islands = 0
        visited = set() # we store (c, r) in visited
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == "1" and (c, r) not in visited:
                    self.bfs(self.grid, r, c, visited)
                    num_of_islands += 1
        return num_of_islands
        

    def bfs(self, grid, r, c, visited):
        q = deque()
        q.append((c, r))
        while q:
            cell = q.popleft()
            if cell not in visited: # this line is important for very big cases, to not run into TLE
                visited.add(cell)
                for dir in Dir:
                    neighbour = tuple(sum(coord) for coord in zip(cell, dir.value))
                    if neighbour not in visited and self._within_boundaries(neighbour) and grid[neighbour[1]][neighbour[0]] == "1": # check in visited to not get into endless loops
                        q.append(neighbour)

    def _within_boundaries(self, cell) -> bool: # cell of (c, r)
        col = cell[0]
        row = cell[1]
        if 0 <= col <= len(self.grid[0])-1 and 0 <= row <= len(self.grid)-1:
            return True
        else:
            return False

    # we can write dfs with recursion so it is easier to write
    # we change the values of the cell that we have already visited, so we no need a visited set, save space
    def get_number_of_islands_dfs(self):
        num_of_islands = 0
        for r in range(len(self.grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(self.grid, r, c)
                    num_of_islands += 1
        return num_of_islands

    def dfs(self, grid, r, c):
        if len(grid)-1 < r or r < 0 or len(grid[0])-1 < c or c < 0 or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        for dir in Dir:
            self.dfs(grid, r+dir.value[1], c+dir.value[0])



if __name__ == "__main__":
    solution = Solution(grid)
    print(solution.get_number_of_islands())
    print(solution.get_number_of_islands_dfs())