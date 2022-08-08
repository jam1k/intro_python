# Write your solution here
import copy
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

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    result = copy.deepcopy(sudoku)
    result[row_no][column_no] = number
    return result

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

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)