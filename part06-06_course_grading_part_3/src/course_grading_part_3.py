# Write your solution here
def final_score(name, exam_points, exercise_points):
    total_points = exam_points + exercise_points
    if total_points < 15:
        return 0
    elif total_points < 18:
        return 1
    elif total_points < 21:
        return 2
    elif total_points < 24:
        return 3
    elif total_points < 28:
        return 4
    else:
        return 5

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    
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
        parts = line.replace("\n", "")
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exer[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6])+ int(parts[7])

    
with open(exam_data) as exam_file:
    exams = {}
    for line in exam_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exams[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3])


print(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}")

for id, name in students.items():
    if id in exer:
        grade_exer = int(exer[id]*10/40)
    if id in exams:
        grade_exam = exams[id]
        total = final_score(name, grade_exam, grade_exer)
        print(f"{name:30}{exer[id]:<10}{grade_exer:<10}{grade_exam:<10}{grade_exam + grade_exer:<10}{total:<10}")
