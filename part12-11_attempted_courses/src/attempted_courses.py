class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

def names_of_students(attempts: list):
    names = map(lambda t: t.student_name, attempts)
    return list(names)

def course_names(attempts: list):
    courses = map(lambda t: t.course_name, attempts)
    return sorted(list(set(courses)))