# Write your solution here
def column_correct(sudoku: list, column_no: int):
    i = 0
    while (i < 9):
        j = i + 1
        while (j < 9):
            if (sudoku[i][column_no] == sudoku[j][column_no] and sudoku[i][column_no] != 0):
                return False
            else:
                j += 1
        i += 1
    return True