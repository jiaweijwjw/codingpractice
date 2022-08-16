# https://leetcode.com/problems/unique-paths/

directions = [(1,0),(0,1)] # right and down
class Solution():
    def __init__(self) -> None:
        pass

    # we start from the destination
    # for every cell, we know that the number of paths to the destination is the number of paths from i can go from right + bottom
    # hence we work backwards, starting from the destination and calculate how many paths from those nearest to the destination all the way to starting pt
    def get_num_unique_paths(self, m, n): # m is num rows, c is num cols
        grid = [[0]*n for _ in range(m)] # this is our dp cache
        # init
        grid[m-1][n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r != m-1 and c != n-1:
                    bottom = grid[r+1][c]
                    right = grid[r][c+1]
                elif r != m-1: # last col but not last row
                    bottom = grid[r+1][c]
                    right = 0
                elif c != n-1: # last row but not last col
                    bottom = 0
                    right = grid[r][c+1]
                else: # r == m-1 and c == n-1
                    continue # destination
                grid[r][c] = bottom + right
        return(grid[0][0])

if __name__ == "__main__":
    solution = Solution()
    inputs = [(3,7),(3,2)] #outputs: 28, 3
    for m, n in inputs:
        print(solution.get_num_unique_paths(m, n))