# Write your solution here

from operator import sub


def add_student(students: dict, name: str):
    students[name] = []

def print_no_courses():
    print(" no completed courses")

def print_no_such_person(name: str):
    print(f"{name}: no such person in the database")

def return_completed(students: dict, name: str):
    completed = 0
    for course in students[name]:
        if course[1]:
            completed += 1
    return completed

def return_sum(students: dict, name: str):
    sum = 0
    for course in students[name]:
        if course[1]:
            sum += course[1]
    return sum

def return_average(students: dict, name: str):
    sum = return_sum(students, name)
    completed = return_completed(students, name)
    if completed != 0:
        average = sum / completed
        return average
    else:
        return 0

def print_courses(students, name):
    completed_courses = return_completed(students, name)
    if completed_courses == 0:
        print_no_courses()
    else:
        print (f" {completed_courses} completed courses:")
        for course in students[name]:
            if course[1] != 0:
                print(f"  {course[0]} {course[1]}")

        average = return_average(students, name)
        print (f" average grade {average:.1f}")


def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}:")
        if (len(students[name]) == 0):
            print_no_courses()
        else:
            print_courses(students, name)
            
    else:
        print_no_such_person(name)

def update_in_alist(alist, key, value):
    return [(k,v) if (k != key) else (key, value) for (k, v) in alist]

def update_in_alist_inplace(alist, key, value):
    alist[:] = update_in_alist(alist, key, value)

def add_course(students: dict, name: str, course: tuple):
    if len(students[name]) == 0:
        students[name].append(course)
    else:
        courses = [cor[0] for cor in students[name]]
        if course[0] in courses:
            for cor in students[name]:
                if course[0] == cor[0] and course[1] > cor[1]:
                    update_in_alist_inplace(students[name], course[0], course[1])
        else:
            students[name].append(course)

def most_courses(students):
    max = 0
    for student in students:
        completed = return_completed(students, student)
        if completed > max:
            result = student
            max = completed
    return result

def best_average(students):
    max = 0
    for student in students:
        mean = return_average(students, student)
        if mean > max:
            max = mean
            result = student
    return result
    
def summary(students: dict):
    print (f"students {len(students)}")
    most_courses_completed = most_courses(students)
    print(f"most courses completed {return_completed(students, most_courses_completed)} {most_courses_completed}")
    the_best_average  = best_average(students)
    print(f"best average grade {return_average(students, the_best_average)} {the_best_average}")


if __name__ == "__main__":
    students = {}
    add_student(students, "Emily")
    add_student(students, "Peter")
    add_course(students, "Emily", ("Software Development Methods", 4))
    add_course(students, "Emily", ("Software Development Methods", 5))
    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
    add_course(students, "Peter", ("Models of Computation", 0))
    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
    add_course(students, "Peter", ("Introduction to Computer Science", 1))
    add_course(students, "Peter", ("Software Engineering", 3))
    summary(students)