# This program works with two CSV files. One of them contains information about some students on a course:
# id;first;last
# 12345678;peter;pythons
# 12345687;jean;javanese
# 12345699;alice;adder
# The other contains the number of exercises each student has completed each week:
# id;e1;e2;e3;e4;e5;e6;e7
# 12345678;4;1;1;4;5;2;4
# 12345687;3;5;3;1;5;4;6
# 12345699;10;2;2;7;10;2;2
# As you can see above, both CSV files also have a header row, which tells you what each column contains.
# Please write a program which asks the user for the names of these two files, reads the files, 
# and then prints out the total number of exercises completed by each student. 
# write your solution here

if True:
    # user input
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    
with open(student_info) as student_file:
    students = {}
    for line in student_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2].strip()
        
with open (exercise_data) as exercise_file:
    exer = {}
    for line in exercise_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exer[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6])+ int(parts[7])


for id, name in students.items():
    if id in exer:
        result = exer[id]
        print(f"{name} {result}")
