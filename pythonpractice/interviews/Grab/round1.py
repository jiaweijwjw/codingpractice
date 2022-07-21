import enum

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

class Dir(enum. Enum): # (c, r)
    right = 1, 0
    down = 0, 1
    left = -1, 0
    up = 0, -1

class Solution():
    def __init__(self, grid) -> None:
        self.grid = grid

    def get_max_area(self):
        max_area = 0
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 1:
                    area = self._dfs(r, c, 0)
                    max_area = max(area, max_area)
        return max_area

    def _dfs(self, r, c, area):
        if len(self.grid)-1 < r or r < 0 or c < 0 or c > len(self.grid[0])-1 or self.grid[r][c] != 1:
            return area
        self.grid[r][c] = "#" # mark as visited
        area += 1
        for dir in Dir:
            area = self._dfs(r+dir.value[1], c+dir.value[0], area)
        return area


if __name__ == "__main__":
    solution = Solution(grid)
    print(solution.get_max_area())