# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[0,1,2,0],
#           [3,4,5,2],
#           [1,3,1,5]]

matrix = [[1,1,1],[1,0,1],[1,1,1]]

class Solution():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.num_of_rows = len(matrix)
        self.num_of_cols = len(matrix[0])

    def print_matrix(self):
        for row in self.matrix:
            print(row)
        print()

    def set_zeroes(self):
        col_to_zeroes = set()
        row_to_zeroes = set()
        for r in range(self.num_of_rows):
            for c in range(self.num_of_cols):
                if self.matrix[r][c] == 0: # cannot exit early as we have to check every cell
                    row_to_zeroes.add(r)
                    col_to_zeroes.add(c)
        for row in range(self.num_of_rows):
            if row in row_to_zeroes:
                self.matrix[row] = [0]*self.num_of_cols
            else:
                for col in range(self.num_of_cols):
                    if col in col_to_zeroes:
                        self.matrix[row][col] = 0
            
    # this solution will set the whole row to zero and then cause the remaining values to screw up as they will be changed since we are doing in place
    def set_zeroes2(self):
        col_to_zeroes = []
        row_to_zeroes = []
        for r in range(self.num_of_rows):
            for c in range(self.num_of_cols):
                if c in col_to_zeroes:
                    self.matrix[r][c] == 0
                    print(self.matrix[r][c])
                    continue # move right to the next col in this row
                if self.matrix[r][c] == 0:
                    if r not in row_to_zeroes:
                        self.matrix[r] = [0]*self.num_of_cols
                    row_to_zeroes.append(r)
                    col_to_zeroes.append(c)
                    break # exit checking the remaining cols in this row (this break only exits the inner for loop)



solution = Solution(matrix)
solution.print_matrix()
solution.set_zeroes3()
solution.print_matrix()