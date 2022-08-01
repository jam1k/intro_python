# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for line in my_matrix:
        i = 0
        while (i < len(line)):
            if line[i] == element:
                count += 1
            i+=1
    return count
