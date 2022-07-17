# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

matrix = [[1,2,3],
          [4,5,6]]

class Matrix():
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.initial_matrix = matrix

    def reset_original_matrix(self):
        self.matrix = self.initial_matrix

    def get_original_matrix(self):
        return self.matrix

    def print_matrix(self, matrix):
        for row in matrix:
            print(row)
        print()

    def transpose(self): # transpose is basically flipping diagonally
        self.matrix = [list(row) for row in zip(*self.matrix)]

    def create_zeroes_matrix(self):
        return [[0 for _ in range(len(self.matrix[0]))] for _ in range(len(self.matrix))]

    def clone_matrix(self):
        return [row[:] for row in self.matrix]

    def reverse_rows(self):
        self.matrix.reverse()
    
    def reverse_columns(self):
        for row in self.matrix:
            row.reverse()

    def _swap(self, r, c): # for flipping diagonally manually
        temp = self.matrix[r][c]
        self.matrix[r][c] = self.matrix[c][r]
        self.matrix[c][r] = temp

    def _flip_diagonally(self):
        # using transpose for the more general case as it can be done to non-square matrixes too
        self.transpose()
        # to flip manually (in place):
        # for r in range(len(self.matrix)):
        #     for c in range(r+1, len(self.matrix[0])): #
        #         self._swap(r, c)

    def rotate_clockwise(self): # reverse rows then flip diagonally
        self.reverse_rows()
        self._flip_diagonally()

    def rotate_anticlockwise(self): # reverse columns then flip diagonally
        self.reverse_columns()
        self._flip_diagonally()  


if __name__ == "__main__":
    my_matrix = Matrix(matrix)
    print("original")
    my_matrix.print_matrix(my_matrix.get_original_matrix())
    my_matrix.transpose()
    print("tranpose")
    my_matrix.print_matrix(my_matrix.get_original_matrix())
    print("zeroes matrix")
    my_matrix.print_matrix(my_matrix.create_zeroes_matrix())
    print("clone matrix")
    my_matrix.print_matrix(my_matrix.clone_matrix())
    my_matrix.reverse_rows()
    print("reverse rows")
    my_matrix.print_matrix(my_matrix.get_original_matrix())
    my_matrix.reverse_columns()
    print("reverse columns")
    my_matrix.print_matrix(my_matrix.get_original_matrix())
    my_matrix.reset_original_matrix()
    print("reset to initial matrix")
    my_matrix.print_matrix(my_matrix.get_original_matrix())
    my_matrix.rotate_clockwise()
    print("rotate clockwise")
    my_matrix.print_matrix(my_matrix.get_original_matrix())
    my_matrix.rotate_anticlockwise()
    print("rotate anti clockwise")
    my_matrix.print_matrix(my_matrix.get_original_matrix())