# Write your solution here
from fileinput import filename


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
def reading_student_info(student_info: str):
    with open(student_info) as student_file:
        students = {}
        for line in student_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1] + " " + parts[2].strip()
    student_file.close()
    return students

def reading_exercise_data(exercise_data: str):
    with open (exercise_data) as exercise_file:
        exer = {}
        for line in exercise_file:
            parts = line.replace("\n", "")
            parts = line.split(';')
            if parts[0] == "id":
                continue
            exer[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6])+ int(parts[7])
    exercise_file.close()
    return exer

def reading_exam_data(exam_data: str):
    with open(exam_data) as exam_file:
        exams = {}
        for line in exam_file:
            parts = line.split(';')
            if parts[0] == "id":
                continue
            exams[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3])
    exam_file.close()
    return exams

def reading_course_data(course_data: str):
    with open(course_data) as course_file:
        course = {}
        for line in course_file:
            parts = line.split(":")
            if parts[0] == "name":
                name = parts[1].strip()
            else:
                study_credits = parts[1].strip()
        course[name] = study_credits
    course_file.close()
    return course

def write_statistics(students, exer, exams, course_info):
    with open("results.txt", "w") as f1, open("results.csv", "w") as f2:
        for course_name in course_info:
            string = f"{course_name}, {course_info[course_name]} credits"
            f1.write(string + "\n")
            f1.write(len(string) * "=" + "\n")

        f1.write(f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n")
        for id, name in students.items():
            if id in exer:
                grade_exer = int(exer[id]*10/40)
            if id in exams:
                grade_exam = exams[id]
                total = final_score(name, grade_exam, grade_exer)
                f1.write(f"{name:30}{exer[id]:<10}{grade_exer:<10}{grade_exam:<10}{grade_exam + grade_exer:<10}{total:<10}\n")
                f2.write(f"{id};{name};{total}\n")
    f1.close()
    f2.close()
    print("Results written to files results.txt and results.csv")

if True:
    # user input
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"
    course_data = "course1.txt"
 
students = reading_student_info(student_info)
exer = reading_exercise_data(exercise_data)
exams = reading_exam_data(exam_data)
course_info = reading_course_data(course_data)

write_statistics(students, exer, exams, course_info)

    
