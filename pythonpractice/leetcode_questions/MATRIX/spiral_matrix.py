matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

directions = [(1,0), (0,1), (-1,0), (0,-1)] # (c, r) or (x, y). right, down, left, right

# this question is not difficult conceptually but there is alot of nitty gritty details that we must check
# the solution is very prone to bugs of boundaries checking, make sure you dont make any careless mistakes
class Solution():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.dir = 0 # start with right direction
        self.top = 1 # initial top should be the second row already
        self.bottom = len(matrix)-1
        self.right = len(matrix[0])-1
        self.left = 0
        self.matrix_size = len(matrix)*len(matrix[0])
        # if < top or < left or > bottom or > right, exceeded the boundary

    def spiral_matrix(self):
        ans = []
        self.spiral(ans, 0, 0)
        return ans

    def is_boundary(self, r, c, dir) -> bool:
        if dir == 0: # currently going right
            if c == self.right:
                return True
        elif dir == 1: # currently going down
            if r == self.bottom:
                return True
        elif dir == 2: # currently going left
            if c == self.left:
                return True
        elif dir == 3: # currently going up
            if r == self.top:
                return True
        else:
            return False

    def set_boundary(self, dir):
        if dir == 0: # going right and hit the right wall, reduce the right wall and turn
            self.right -= 1
        elif dir == 1: # going down and hit the bottom wall, reduce the bottom wall and turn
            self.bottom -= 1
        elif dir == 2: # going left and hit the left wall, reduce the left wall and turn
            self.left -= 1
        elif dir == 3: # going up and hit the top wall, reduce the top wall and turn
            self.top -= 1
        else:
            pass

    def spiral(self, ans, r, c):
        if len(ans) == self.matrix_size: # end of spiral
            return
        ans.append(self.matrix[r][c])
        if self.is_boundary(r, c, self.dir):
            self.set_boundary(self.dir)
            self.dir = (self.dir+1)%4
        next_r = r + directions[self.dir][1]
        next_c = c + directions[self.dir][0]
        self.spiral(ans, next_r, next_c)
        


if __name__ == "__main__":
    solution = Solution(matrix)
    print(solution.spiral_matrix())