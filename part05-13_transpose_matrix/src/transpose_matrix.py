# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. 
# The function should transpose the matrix. 
# Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.
# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.
# Write your solution here

def transpose(matrix: list):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]
    matrix.clear()
    for line in result:
        matrix.append(line[:])

if __name__ == "__main__":
    matrix = [[1, 2], [1, 2]]
    transpose(matrix)
    print(matrix)