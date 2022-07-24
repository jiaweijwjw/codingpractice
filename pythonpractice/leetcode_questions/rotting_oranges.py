from collections import deque

# grid = [[2,1,1],
#         [1,1,0],
#         [0,1,1]]
grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]

directions = [(1,0), (0,1), (-1,0), (0,-1)]

class Solution():
    def __init__(self, grid) -> None:
        self.grid = grid

    # firstly, lets consider normal bfs on grids, in this case we will encounter some edge cases that will produce an incorrect result
    # imagine we have a group of oranges that can be reached. think of the oranges as a connected graph
    # if we have >1 rotten orange, the time needed would be lesser as they would spread faster
    # to solve this problem, we can consider using an outer while loop to spread once to neighbours for all rotten oranges
    # and then return the number of times the while loop runs
    # this way of doing it is very brute force as we will need to go through the grid for many times
    # when doing matrixes and graphs, try to think of solutions that can just iterate through the grid once

    # the way we will solve this question is:
    # we iterate through the entire graphs and add all rotten oranges to the bfs queue, and also collect the count of the number of fresh oranges
    # then we will do bfs for the queue, but everytime we popleft from the queue, we check if there is any fresh oranges left
    # note that we are doing bfs level by level like a water ripple. meaning time only increase by 1 for everything in the same level
    # if we do it the normal bfs traversal way, if there are 2 nodes on the same level, time will be added twice which is incorrect
    # if it fulfils the condition, then we will rot the 4 neighbouring oranges
    # to rot the neighbouring oranges, we will first check if it is already rotten (visited)
    # only if the neighbouring orange is a fresh orange, we will decrease the fresh orange count
    # dont forget to check for boundaries
    def get_minutes_till_all_rotten(self):
        time = 0
        q = deque()
        num_fresh_oranges = 0
        # iterate once to get the number of fresh oranges and populate the bfs queue with rotten oranges
        for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
                if self.grid[r][c] == 1:
                    num_fresh_oranges += 1
                elif self.grid[r][c] == 2:
                    q.append((c, r))
        # do the bfs here
        if num_fresh_oranges == 0: # this is a special edge case where there is no oranges
            return 0
        while q and num_fresh_oranges > 0:
            time += 1
            for _ in range(len(q)): # pop out everything in the same bfs level
                c, r = q.popleft()
                for dir in directions:
                    neighbour_c = c + dir[0]
                    neighbour_r = r + dir[1]
                    if self._within_bounds(neighbour_c, neighbour_r) and self.grid[neighbour_r][neighbour_c] == 1:
                        self.grid[neighbour_r][neighbour_c] = 2 # rot this orange
                        num_fresh_oranges -= 1
                        q.append((neighbour_c, neighbour_r))
        if num_fresh_oranges > 0:
            return -1 # if there is fresh oranges but not connected to any rotten oranges, impossible to rot them
        else:
            return time

    def _within_bounds(self, c, r):
        if 0 <= c <= len(self.grid[0])-1 and 0 <= r <= len(self.grid)-1:
            return True
        return False


if __name__ == "__main__":
    solution = Solution(grid)
    print(solution.get_minutes_till_all_rotten())