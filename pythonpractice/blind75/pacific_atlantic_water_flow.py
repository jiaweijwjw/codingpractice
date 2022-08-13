# https://leetcode.com/problems/pacific-atlantic-water-flow/

directions = [(0,1),(1,0),(0,-1),(-1,0)]

class Solution():
    def __init__(self) -> None:
        pass

    def get_cells_that_can_reach_both_oceans(self, island):
        ans = []
        can_reach_atlantic = set()
        can_reach_pacific = set()
        for r in range(len(island)):
            for c in range(len(island[0])):
                if r == 0 or c == 0:
                    self._dfs_from_ocean(island, r, c, can_reach_pacific)
                if r == len(island)-1 or c == len(island[0])-1: # cannot use elif
                    self._dfs_from_ocean(island, r, c, can_reach_atlantic)
        for cell in can_reach_atlantic:
            if cell in can_reach_pacific:
                ans.append([cell[1], cell[0]])
        return ans

    def _dfs_from_ocean(self, island, r, c, visited):
        visited.add((c, r))
        for dir in directions:
            neighbour_c = c + dir[0]
            neighbour_r = r + dir[1]
            if self._within_bounds(island, neighbour_r, neighbour_c) and (neighbour_c, neighbour_r) not in visited and island[neighbour_r][neighbour_c] >= island[r][c]:
                self._dfs_from_ocean(island, neighbour_r, neighbour_c, visited)

    def _within_bounds(self, island, r, c):
        return 0 <= r <= len(island)-1 and 0 <= c <= len(island[0])-1


if __name__ == "__main__":
    solution = Solution()
    inputs = [
        [[1, 2, 2, 3, 5],
         [3, 2, 3, 4, 4],
         [2, 4, 5, 3, 1],
         [6, 7, 1, 4, 5],
         [5, 1, 1, 2, 4]],

        [[2, 1], [1, 2]]
    ]
    # outputs: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]], [[0,0],[0,1],[1,0],[1,1]]
    for island in inputs:
        print(solution.get_cells_that_can_reach_both_oceans(island))