# The file matrix.txt contains a matrix. Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.
# 
# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. 
# Write your solution here

def reading_file(filename):
    result = []
    lines = []
    with open(filename) as my_file:
        for line in my_file:
            line = line.split(",")
            lines = [int(num) for num in line]
            result.append(lines)
    return result

def row_sums():
    matrix = reading_file("matrix.txt")
    return [sum(line) for line in matrix]

def matrix_sum():
    return (sum(row_sums()))

def matrix_max():
    matrix = reading_file("matrix.txt")
    row_maxes = [max(line) for line in matrix]
    return (max(row_maxes))
