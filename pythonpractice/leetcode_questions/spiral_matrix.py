import enum
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1],[2],[3],[4]]
# matrix = [[1,2,3,4]]
# matrix = [[1]]

# i think a better way to do this is to use a list of tuples (x, y)
class Direction(enum.Enum):
    right = (1, 0) # (x, y) direction
    down = (0, 1)
    left = (-1, 0)
    up = (0, -1)

class Solution():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.matrix_size = len(matrix)*(len(matrix[0]))
        self.ans = []
        self.direction = Direction.right
        self.first_col_index = 0
        self.last_col_index = len(matrix[0])-1
        self.first_row_index = 0
        self.last_row_index = len(matrix)-1
    
    def print_ans(self):
        print(self.ans)

    # recursive spiral
    def spiral(self, x, y):
        print(x, y, self.matrix[y][x])
        self.ans.append(self.matrix[y][x]) # y in row and x is col, dont be careless
        if len(self.ans) == self.matrix_size: # spiral ended
            return
        if self.direction == Direction.right:
            print("right")
            if x == self.last_col_index:
                print("going down")
                self.direction = Direction.down
                self.first_row_index += 1
                self.spiral(x + Direction.down.value[0], y + Direction.down.value[1])
            else: # continue right
                self.spiral(x + Direction.right.value[0], y + Direction.right.value[1])
        elif self.direction == Direction.down:
            print("down")
            if y == self.last_row_index:
                print("going left")
                self.direction = Direction.left
                self.last_col_index -= 1
                self.spiral(x + Direction.left.value[0], y + Direction.left.value[1])
            else: # continue down
                self.spiral(x + Direction.down.value[0], y + Direction.down.value[1])
        elif self.direction == Direction.left:
            print("left")
            if x == self.first_col_index:
                print("going up")
                self.direction = Direction.up
                self.last_row_index -= 1
                self.spiral(x + Direction.up.value[0], y + Direction.up.value[1])
            else: # continue left
                self.spiral(x + Direction.left.value[0], y + Direction.left.value[1])
        else: # up
            print("up")
            if y == self.first_row_index:
                print("going right")
                self.direction = Direction.right
                self.first_col_index += 1
                self.spiral(x + Direction.right.value[0], y + Direction.right.value[1])
            else: # continue up
                self.spiral(x + Direction.up.value[0], y + Direction.up.value[1])


solution = Solution(matrix)
solution.spiral(0, 0)
solution.print_ans()