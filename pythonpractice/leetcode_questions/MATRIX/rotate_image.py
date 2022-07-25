# for rotating images / matrix, the following 2 methods are the common solutions
# swap symmetry refers to swapping [i][j] with [j][i]

# /*
#  * clockwise rotate
#  * first reverse up to down, then swap the symmetry 
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3
# */

# /*
#  * anticlockwise rotate
#  * first reverse left to right, then swap the symmetry
#  * 1 2 3     3 2 1     3 6 9
#  * 4 5 6  => 6 5 4  => 2 5 8
#  * 7 8 9     9 8 7     1 4 7
# */

matrix = [[1,2,3],[4,5,6],[7,8,9]]

class Solution():
    def __init__(self, matrix) -> None:
        self.matrix = matrix

    def swap(self, r, c):
        temp = self.matrix[r][c]
        self.matrix[r][c] = self.matrix[c][r]
        self.matrix[c][r] = temp

    def rotate_clockwise(self):
        self.matrix.reverse()
        for r in range(len(self.matrix)):
            for c in range(r+1, len(self.matrix[0])):
                self.swap(r, c)

    def rotate_anticlockwise(self):
        for row in self.matrix:
            row.reverse()
        # note that we swap along the diagonal lines
        for r in range(len(self.matrix)):
            for c in range(r+1, len(self.matrix[0])):
                self.swap(r, c)

    def print_matrix(self):
        for row in self.matrix:
            print(row)

if __name__ == "__main__":
    solution = Solution(matrix)
    solution.print_matrix()
    print()
    solution.rotate_clockwise()
    solution.print_matrix()
    print()
    solution.rotate_anticlockwise()
    solution.print_matrix() # back to original matrix
    print()
    solution.rotate_anticlockwise()
    solution.print_matrix()