# https://leetcode.com/problems/rotting-oranges/

from collections import deque

directions = [(0,1),(1,0),(0,-1),(-1,0)]

class Solution():
    def __init__(self) -> None:
        pass

    def get_min_time_till_no_fresh_oranges(self, grid):
        q = deque()
        fresh_count = 0
        time_elapsed = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: # fresh
                    fresh_count += 1
                elif grid[r][c] == 2: # rotten
                    q.append((c, r))
        if fresh_count == 0:
            return 0
        while q and fresh_count > 0:
            time_elapsed += 1
            for _ in range(len(q)):
                c, r = q.popleft()
                for dir in directions:
                    neighbour_c = c + dir[0]
                    neighbour_r = r + dir[1]
                    if self._within_bounds(grid, neighbour_r, neighbour_c) and grid[neighbour_r][neighbour_c] == 1:
                        grid[neighbour_r][neighbour_c] = 2
                        q.append((neighbour_c, neighbour_r))
                        fresh_count -= 1
        if fresh_count > 0:
            return -1
        return time_elapsed

    def _within_bounds(self, grid, r, c):
        return 0 <= r <= len(grid)-1 and 0 <= c <= len(grid[0])-1




if __name__ == "__main__":
    solution = Solution()
    inputs = [
        [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]],

        [[2, 1, 1],
         [0, 1, 1],
         [1, 0, 1]],

        [[0, 2]]
    ]
    # outputs: 4, -1, 0
    for grid in inputs:
        print(solution.get_min_time_till_no_fresh_oranges(grid))
