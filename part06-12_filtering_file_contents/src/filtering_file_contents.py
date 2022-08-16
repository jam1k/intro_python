# Write your solution here

def reading_file(filename):
    result = []
    with open(filename) as f:
        for line in f:
            line = line.replace("\n", "")
            parts = line.split(';')
            parts[2] = int(parts[2])
            result.append(parts)
    f.close()
    return result

def writing_file(filename:str, data):
    with open(filename, "w") as f:
        for line in data:
            string = ";".join(map(str, line))
            f.write(string + "\n")
    f.close()

def is_correct_solution(line: list):
    if eval(line[1]) == line[2]:
        return True
    else:
        return False


def filter_solutions():
    solutions = reading_file("solutions.csv")
    correct = []
    incorrect = []
    for line in solutions:
        if is_correct_solution(line):
            correct.append(line)
        else:
            incorrect.append(line)
    writing_file("correct.csv", correct)
    writing_file("incorrect.csv", incorrect)

if __name__ == "__main__":
    filter_solutions()
