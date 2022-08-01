# Write your solution here
def row_correct(sudoku: list, row_no: int):
    i = 0
    while (i < 9):
        j = i + 1
        while (j < 9):
            print(sudoku[row_no][i] == sudoku[row_no][j])
            print(sudoku[row_no][i] != 0)
        
            if (sudoku[row_no][i] == sudoku[row_no][j] and sudoku[row_no][i] != 0):
                return False
            else:
                j += 1
        i += 1
    return True

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

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    i = row_no
    
    while (i < row_no + 3):
        j = column_no
        while (j < column_no + 3):
            number = sudoku[i][j]        
            if number > 0 and number in numbers:
                return False
            else:
                numbers.append(number)
                j += 1
        i+=1

    return True
def sudoku_grid_correct(sudoku: list):
    line = 0
    while (line < 9):
        if (not row_correct(sudoku, line)):
            return False
        line += 1
    
    column = 0
    while (column < 9):
        if (not column_correct(sudoku, column)):
            return False
        column += 1
    
    if ((not block_correct(sudoku, 0, 0)) or 
        (not block_correct(sudoku, 0, 3)) or
        (not block_correct(sudoku, 0, 6)) or
        (not block_correct(sudoku, 3, 0)) or
        (not block_correct(sudoku, 3, 3)) or
        (not block_correct(sudoku, 3, 6)) or
        (not block_correct(sudoku, 6, 0)) or
        (not block_correct(sudoku, 6, 3)) or
        (not block_correct(sudoku, 6, 6))):
        return False
    return True

