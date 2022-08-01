# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "/Users/jamilya/Library/Application Support/tmc/vscode/mooc-programming-22/part06-04_course_grading_part_1/src/students1.csv"
    exercise_data = "/Users/jamilya/Library/Application Support/tmc/vscode/mooc-programming-22/part06-04_course_grading_part_1/src/exercises1.csv"
    
with open(student_info) as student_file:
    students = {}
    for line in student_file:
        #line = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2].strip()
        #print(f"{parts[2]}")

with open (exercise_data) as exercise_file:
    exer = {}
    for line in exercise_file:
        parts = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exer[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6])+ int(parts[7])


for id, name in students.items():
    if id in exer:
        result = exer[id]
        print(f"{name} {result}")
