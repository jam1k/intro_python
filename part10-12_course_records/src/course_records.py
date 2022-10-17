# tee ratkaisusi tänne

from email.mime import application


class CourseRecords:
    def __init__(self):
        self.__courses = {}
    
    def add_course(self, course, grade, credits):
        if not course in self.__courses:
            self.__courses[course] = (grade, credits)
        else:
            if self.__courses[course][0] < grade:
                self.__courses[course] = (grade, credits)

    def get_course_data(self, course):
        if not course in self.__courses:
            return f"no entry for this course"
        else:
            return f"{course} ({self.__courses[course][1]} cr) grade {self.__courses[course][0]}"
    
    def statistics(self):
        if len (self.__courses) != 0:

            credits_total = 0
            grade_total = 0
            counter1 = 0
            counter2 = 0
            counter3 = 0
            counter4 = 0
            counter5 = 0
            
            for item in self.__courses:
                credits_total += self.__courses[item][1]
                grade_total += self.__courses[item][0]
                if self.__courses[item][0] == 1:
                    counter1 += 1
                elif self.__courses[item][0] == 2:
                    counter2 += 1
                elif self.__courses[item][0] == 3:
                    counter3 += 1
                elif self.__courses[item][0] == 4:
                    counter4 += 1
                elif self.__courses[item][0] == 5:
                    counter5 += 1

            grade_mean = grade_total / len(self.__courses)
            formated_mean = "{:.1f}".format(grade_mean)
            first = f"{len(self.__courses)} completed courses, a total of {credits_total} credits"
            
            second = f"mean {formated_mean}"
            third = f"grade distribution"
            fourth = f"5: {'x'* counter5}"
            fifth = f"4: {'x'* counter4}"
            sixth = f"3: {'x'* counter3}"
            seventh = f"2: {'x'* counter2}"
            eight = f"1: {'x'* counter1}"

            return first + "\n" + second  + "\n" + third  + "\n" +  fourth  + "\n" + fifth  + "\n" + sixth  + "\n" + seventh  + "\n" +  eight

        


class CourseRecordsApplication:
    def __init__(self):
        self.__courses = CourseRecords()


    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
    
    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits =  int(input("credits: "))
        self.__courses.add_course(course, grade, credits)

    def get_data(self):
        course = input("course: ")
        print(self.__courses.get_course_data(course))
    
    def stat(self):
        stats = self.__courses.statistics()
        print(stats)
    
    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_data()
            elif command == "3":
                self.stat()
            else:
                self.help()

app = CourseRecordsApplication()
app.execute()
