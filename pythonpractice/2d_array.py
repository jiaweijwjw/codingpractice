grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

board = [[0, 1, 0, 0],
         [1, 0, 0, 1],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]

board2 = [["X", "X", "X", "X"], # X win
          ["O", "O", "X", "O"],
          ["O", "X", "X", "O"],
          ["O", "O", "O", "X"]]

board3 = [["X", "X", "X", "."], # ongoing
          ["O", "O", "X", "O"], # nobody win yet, but not filled
          ["O", "X", "X", "O"],
          ["O", "O", "O", "X"]]
    
board4 = [["O", "X", "X", "O"], # O win diagonal
          ["X", "X", "O", "O"],
          ["O", "O", "X", "O"],
          ["O", "O", "O", "X"]]

board5 = [["X", "X", "X", "O"], # tie
          ["O", "O", "X", "O"], # everything filled but nobody wins
          ["O", "X", "X", "O"],
          ["O", "O", "O", "X"]]

board6 = [["O", "X", "X", "O"], # O win column
          ["O", "O", "X", "O"], 
          ["O", "X", "X", "O"],
          ["O", "O", "O", "X"]]

# A player wins if it has a complete row, col or the 2 diagonals
# check if any row or col all same player
# check if any of the 2 diagonals all same player
# anything below means nobody wins
# else check if "." exists, if yes means ongoing
# if not, it is a tie
# is it possible to only go through the board once

def check_row(board, row_n, col_n):
    winner = None
    empty_slot = False
    for row in range(row_n):
        all_same = True
        first = board[row][0]
        if "." in board[row]:
            empty_slot = True
            continue # no need to check this row
        else:
            for col in range(1, col_n):
                if board[row][col] != first:
                    all_same = False
                    break # no need to continue checking this row
        if all_same == True: # all same for one row, there is a winner
            winner = first
            return winner, empty_slot
    return winner, empty_slot

def check_col(board, row_n, col_n):
    """ for each column, check if it is the same as the val in the first row col value """
    winner = None
    empty_slot = False
    for col in range(col_n):
        all_same = True
        first = board[0][col]
        for row in range(1, row_n):
            if board[row][col] == ".":
                empty_slot = True
                break
            if board[row][col] != first:
                all_same = False
                break
        if all_same == True:
            winner = first
            return winner, empty_slot
    return winner, empty_slot

def check_diagonals(board, row_n):
    first_diagonal1 = board[0][0] # diagonal from top left to btm right
    first_diagonal2 = board[0][row_n-1] # diagonal from top right to btm left
    all_same1, all_same2 = True, True
    for i in range(1, row_n):
        if board[i][i] != first_diagonal1:
            all_same1 = False
        if board[i][row_n-1-i] != first_diagonal2:
            all_same2 = False
    if not all_same1 and not all_same2:
        return
    elif all_same1:
        return first_diagonal1
    else:
        return first_diagonal2



def tic_tac_toe(board): # row and col are iterators
    col_n = len(board[0])
    row_n = len(board)
    has_empty = False
    winner, empty_slot = check_row(board, row_n, col_n)
    if empty_slot == True: has_empty = True
    if winner == None: # no winner after checking rows
        winner, empty_slot = check_col(board, row_n, col_n) # check columns next
        if empty_slot == True: has_empty = True
        if winner == None: # still no winner after checking columns
            winner = check_diagonals(board, row_n) # check diagonals next
            if winner: # there is a winner after checking diagonals
                print(winner)
            else: # check the board if got empty slot to determine ongoing or tie (game ended)
                if has_empty:
                    print("ongoing")
                else:
                    print("tie")
        else: # there is a winner when checking the columns
            print(winner)
    else: # there is a winner when checking the rows
        print(winner)

tic_tac_toe(board2)
tic_tac_toe(board3)
tic_tac_toe(board4)
tic_tac_toe(board5)
tic_tac_toe(board6)
    






# n = len(board)

# def check_board(board):
#     for row in range(n):
#         row_count = 0
#         for col in range(n):
#             row_count += board[row][col]
#         if row_count >1:
#             return False
#     for col in range(n):
#         col_count = 0
#         for row in range(n):
#             col_count += board[row][col]
#         if col_count >1:
#             return False
#     return True

# print(check_board(board))