# In this exercise we will complete two more functions for the sudoku project from the previous section: print_sudoku and add_number.
# The function print_sudoku(sudoku: list) takes a two-dimensional array representing a sudoku grid as its argument. The function should print out the grid in the format specified in the examples below.
# The function add_number(sudoku: list, row_no: int, column_no: int, number:int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should add the digit to the specified location in the grid.
# Write your solution here

def print_sudoku(sudoku: list):
    result = []
    for i, line in enumerate(sudoku):
        for j, num in enumerate(line):
            if j % 3 == 0 and j != 0:
                print (" ", end = "")
            if (num == 0):
                print("_ ", end = "")
            else:
                print(f"{num} ", end = "")
        print ("\n", end = "")
        if (i + 1) % 3 == 0:
            print ("\n", end = "")

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

if __name__ == "__main__":
    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)