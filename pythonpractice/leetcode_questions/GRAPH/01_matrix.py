from collections import deque

# grid= [[0,0,0], # [[0,0,0]
#        [0,1,0], #  [0,1,0]
#        [1,1,1]] #  [1,2,1]]

grid = [[0,1,1,1,1], # [[0,1,2,3,4],
        [1,1,1,1,1], # [[1,2,3,4,3],
        [1,1,1,1,1], # [[2,3,4,3,2],
        [1,1,1,1,1], # [[3,4,3,2,1],
        [1,1,1,1,0]] # [[4,3,2,1,0]]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution():
    def __init__(self, grid) -> None:
        self.grid = grid

    def find_nearest_zero(self):
        q = deque() 
        visited = set()
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 0:
                    visited.add((c ,r))
                    q.append((c, r))
        while q:
            col, row = q.popleft()
            for dir in directions:
                neighbour_c = col+dir[0]
                neighbour_r = row+dir[1]
                if self._within_bounds(self.grid, neighbour_r, neighbour_c) and (neighbour_c, neighbour_r) not in visited:
                    self.grid[neighbour_r][neighbour_c] = self.grid[row][col] + 1
                    visited.add((neighbour_c, neighbour_r))
                    q.append((neighbour_c, neighbour_r))

    def _within_bounds(self, grid, r, c):
        return 0 <= r <= len(grid)-1 and 0 <= c <= len(grid[0])-1

    def print_grid(self):
        for row in self.grid:
            print(row)

if __name__ == "__main__":
    solution = Solution(grid)
    solution.print_grid()
    solution.find_nearest_zero()
    solution.print_grid()