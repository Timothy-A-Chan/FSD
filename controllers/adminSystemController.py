from models.database import Database as db

class AdminSystemController:

    def clearDatabase(self):
        pass

    def groupStudents(self):
        print("Grade Grouping")
        students = db.read()

        grade_order = {
        "HD": 4,
        "D": 3,
        "C": 2,
        "P": 1,
        "Z": 0,
        }

        for student in students:
            total = sum(subject.mark for subject in student.subjects)
            average = total / len(student.subjects)

                # Assign grade based on average
            if average >= 85:
                student.grade = "HD"
            elif 75 <= average < 85:
                student.grade = "D"
            elif 65 <= average < 75:
                student.grade = "C"
            elif 50 <= average < 65:
                student.grade = "P"
            else:
                student.grade = "Z"

            student.mark = average

            students.sort(key=lambda s: grade_order.get(s.mark), reverse=True)

            db.write(students)

            for student in students:
                print(f"{student.grade} --> [{student.name} :: {str(student.id)} --> Grade: {student.mark:.2f}]")

    def partitionStudents(self):
        pass

    def removeStudents(self):
        pass

    def show(self):
        print("Student List")
        students = db.read()
        for student in students:
            print(student.name + " :: " + str(student.id) + " --> Email: " + student.email)

    def system(self):
        userInput = input("\033[96mAdmin System (c/g/p/r/s/x): \033[0m")

        while(userInput != "x"):
            match userInput:
                case "c":
                    self.clearDatabase()

                case "g":
                    self.groupStudents()

                case "p":
                    self.partitionStudents()

                case "r":
                    self.removeStudents()

                case "s":
                    self.show()
                case _:
                    pass
            userInput = input("\033[96mAdmin System (c/g/p/r/s/x): \033[0m")