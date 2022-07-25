board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] # valid / true

board2 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]] # invalid / false

# the following solution is an O(n^2) solution whereby we iterate through each element in the board
# if there is any element that does not obey the rule of a valid board, we return False immediately
# else, if the enter board is checked and not rules are broken, the board is a valid board
# the 3 rules are:
# no repeated number in a row
# no repeated number in a column
# no repeated number in a subgrid
# one trick that we can use to check for existence is to use a set. recall that a set can store tuples and different types
# hence we can just use a single set to store existence in all 3 constraints, the row, col and subgrids
# another trick is using floor division to get the subgrid that an element is in

class Solution():
    def __init__(self, board) -> None:
        self.board = board

    def check_valid_board(self):
        checked = set()
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                val = self.board[r][c]
                if val != ".":
                    if ("row", r, val) not in checked and ("col", c, val) not in checked and ("subgrid", r//3, c//3, val) not in checked:
                        checked.add(("row", r, val))
                        checked.add(("col", c, val))
                        checked.add(("subgrid", r//3, c//3, val))
                    else: # clash in set, disobeys 3 rules
                        return False
        return True

if __name__ == "__main__":
    solution = Solution(board)
    print(solution.check_valid_board())
    solution2 = Solution(board2)
    print(solution2.check_valid_board())