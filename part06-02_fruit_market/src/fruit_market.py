# write your solution here
def read_fruits():
    result = {}
    with open("fruits.csv") as my_file:
        for line in my_file:
            line = line.replace('\n', '')
            line = line.split(";")
            result[line[0]] = float(line[1])
    return result

