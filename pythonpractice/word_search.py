word_grid = ["helloxz",
             "vvsoche",
             "heohffa"]

word = "ooo"

directions = [(-1, -1), # top left
              (-1,  0), # top
              (-1,  1), # top right
              ( 0, -1), # left
              ( 0,  1), # right
              ( 1, -1), # btm left
              ( 1,  0), # btm
              ( 1,  1)] # btm right


def check_for_word(word_grid, row, col, word):
    if word_grid[row][col] != word[0]: return # doesnt match first char of word
    for x, y in directions:
        is_found = True
        row_dir = row + x
        col_dir = col + y
        for char_i in range(1, len(word)): # dont have to check the first char as it is already checked
            # take note of the order here, have to check boundaries before accessing word_grid indexes
            if (0 <= row_dir < rows) and (0 <= col_dir < cols) and (word[char_i] == word_grid[row_dir][col_dir]): # within grid boundaries
                row_dir += x
                col_dir += y
            else:
                is_found = False
                break
        if is_found: print(f"word is found at slot [{row}, {col}] in the ({x}, {y}) direction.")
        
        
    

def word_search(word_grid, word):
    global rows, cols
    rows = len(word_grid)
    cols = len(word_grid[0])
    for row in range(rows):
        for col in range(cols):
            check_for_word(word_grid, row, col, word)

word_search(word_grid, word)