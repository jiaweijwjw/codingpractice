# https://leetcode.com/problems/01-matrix/

from collections import deque

directions = [(0,1),(1,0),(0,-1),(-1,0)]

class Solution():
    def __init__(self) -> None:
        pass

    def find_nearest_zeroes(self, grid): # modifiy grid in place
        q = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((c, r)) # pre append all 0
                    visited.add((c, r)) # why must i visit first?
        while q:
            c, r = q.popleft()
            # visited.add((c, r))
            for dir in directions:
                neighbour_c = c + dir[1]
                neighbour_r = r + dir[0]
                if self._within_bounds(grid, neighbour_r, neighbour_c) and (neighbour_c, neighbour_r) not in visited:
                    q.append((neighbour_c, neighbour_r))
                    visited.add((neighbour_c, neighbour_r))
                    grid[neighbour_r][neighbour_c] = grid[r][c] + 1
        return grid

    def _within_bounds(self, grid, r, c):
        return 0 <= r <= len(grid)-1 and 0 <= c <= len(grid[0])-1

if __name__ == "__main__":
    solution = Solution()
    inputs = [
        [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 1, 0],
         [1, 1, 1]],


        [[0, 1, 0],
         [0, 1, 0],
         [0, 1, 0]]
    ]
    # outputs: 
    # [[0, 0, 0],
    #  [0, 1, 0],
    #  [0, 0, 0]]

    # [[0, 0, 0],
    #  [0, 1, 0],
    #  [1, 2, 1]]

    # [[0, 1, 0],
    #  [0, 1, 0],
    #  [0, 1, 0]]

    for grid in inputs:
        ans_grid = solution.find_nearest_zeroes(grid)
        for row in ans_grid:
            print(row)
        print()
