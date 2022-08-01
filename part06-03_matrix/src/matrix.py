# write your solution here
def reading_file(filename):
    result = []
    lines = []
    with open(filename) as my_file:
        for line in my_file:
            #line = line.replace("\n", "")
            line = line.split(",")
            lines = [int(num) for num in line]
            result.append(lines)
    return result

def matrix_sum():
    return (sum(row_sums()))

def matrix_max():
    matrix = reading_file("matrix.txt")
    row_maxes = [max(line) for line in matrix]
    return (max(row_maxes))

def row_sums():
    matrix = reading_file("matrix.txt")
    return [sum(line) for line in matrix]

if __name__ == "__main__":
    print(matrix_sum())