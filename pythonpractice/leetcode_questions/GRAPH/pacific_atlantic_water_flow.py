from collections import deque

island = [[1,2,2,3,5],
          [3,2,3,4,4],
          [2,4,5,3,1],
          [6,7,1,4,5],
          [5,1,1,2,4]]
# island = [[2,1],
#           [1,2]]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution():
    def __init__(self, island) -> None:
        self.island = island

    def get_cells_can_reach_both_atlantic_and_pacific(self):
        ans = []
        p_visited = set()
        a_visited = set()

        for r in range(len(self.island)):
            for c in range(len(self.island[0])):
                if r == 0 or c == 0:
                    self._dfs_recursive(self.island, r, c, p_visited)
                if r == len(self.island)-1 or c == len(self.island[0])-1: # cannot use elif, or the 2 cells connected to both pacific and atlantic wont be read twice
                    self._dfs_recursive(self.island, r, c, a_visited)
        for cell in p_visited:
            if cell in a_visited:
                ans.append([cell[1], cell[0]])

        return ans

    def _dfs_recursive(self, island, r, c, visited):
        if (c, r) in visited:
            return
        else:
            visited.add((c, r))
            for dir in directions:
                neighbour_c = c + dir[0]
                neighbour_r = r + dir[1]
                if self._within_bounds(island, neighbour_r, neighbour_c) and island[neighbour_r][neighbour_c] >= island[r][c]:
                    self._dfs_recursive(island, neighbour_r, neighbour_c, visited)

    def _within_bounds(self, island, r, c):
        return 0 <= r <= len(island)-1 and 0 <= c <= len(island[0])-1

if __name__ == "__main__":
    solution = Solution(island)
    print(solution.get_cells_can_reach_both_atlantic_and_pacific())