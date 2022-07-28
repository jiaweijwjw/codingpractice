from collections import deque

island = [[1,2,2,3,5],
          [3,2,3,4,4],
          [2,4,5,3,1],
          [6,7,1,4,5],
          [5,1,1,2,4]]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

class Solution():
    def __init__(self, island) -> None:
        self.island = island

    def water_flow(self):
        ans = []
        for r in range(len(self.island)):
            for c in range(len(self.island[0])):
                if (r == 0 and c == len(self.island[0])-1) or (r == len(self.island)-1 and c == 0):
                    ans.append([r, c])
                    continue
                # print("flow", r, c)
                if self._flow(self.island, r, c):
                    ans.append([r, c])
                # print()
        return ans

    def _flow(self, island, r, c) -> bool:
        can_reach_pacific, can_reach_atlantic = False, False
        s = deque()
        visited = set()
        s.append((c, r))
        while s:
            if can_reach_atlantic and can_reach_pacific: # exit early
                break
            cell = s.pop() # using stack for dfs
            if cell not in visited:
                # print("cell", cell[1], cell[0])
                visited.add(cell)
                cell_c, cell_r = cell
                # can_reach_pacific = self._is_connected_to_pacific(island, cell_r, cell_c) # this will set back to false
                if self._is_connected_to_pacific(island, cell_r, cell_c):
                    can_reach_pacific = True
                if self._is_connected_to_atlantic(island, cell_r, cell_c):
                    can_reach_atlantic = True
                for dir in directions:
                    # neighbour = tuple(sum(i) for i in zip(dir, cell))
                    neighbour_c = cell_c + dir[0]
                    neighbour_r = cell_r + dir[1]
                    if self._within_bounds(island, neighbour_r, neighbour_c) and island[neighbour_r][neighbour_c] <= island[cell_r][cell_c]:
                        s.append((neighbour_c, neighbour_r))
        return can_reach_atlantic and can_reach_pacific

    def _within_bounds(self, island, r, c):
        return 0 <= r <= len(island)-1 and 0 <= c <= len(island[0])-1

    def _is_connected_to_pacific(self, island, r, c):
        return r == 0 or c == 0

    def _is_connected_to_atlantic(self, island, r, c):
        return r == len(island)-1 or c == len(island[0])-1 

if __name__ == "__main__":
    solution = Solution(island)
    print(solution.water_flow())