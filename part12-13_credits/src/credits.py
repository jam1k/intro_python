from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    accepted_courses = filter(lambda t: t.grade >= 1, attempts)
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, accepted_courses, 0)

def average(attempts: list):
    accepted_courses = list(filter(lambda t: t.grade > 0, attempts))
    sum_of_grades = reduce(lambda reduced_sum, attempt: reduced_sum + attempt.grade, accepted_courses, 0)
    return sum_of_grades / len(accepted_courses)

if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Programming Course", 4, 5)
    s3 = CourseAttempt("Algorithms", 3, 0)
    print(average([s1, s2, s3]))