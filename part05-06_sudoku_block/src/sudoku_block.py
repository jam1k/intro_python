# Write your solution here
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

    
if __name__ == "__main__":        
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))