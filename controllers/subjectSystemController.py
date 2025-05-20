from models.subject import Subject
from models.database import Database as db
import random


class SubjectSystemController:

    def __init__(self, student, controller):
        self.student = student
        self.controller = controller
        if self.student.subjects is None:
            self.student.subjects = []

    def changePassword(self):
        print("Updating Password")
        newPassword = input("New Password: ")
        confirmPassword = input("Confirm Password: ")
        if(self.controller.checkPassword(newPassword)):
            if(newPassword != confirmPassword):
                print("Password does not match - try again")
                confirmPassword = input("Confirm Password: ")
            else:
                self.student.password = newPassword
                students = db.read()
                for i, student in enumerate(students):
                    if student.id == self.student.id:
                        students[i] = self.student  
                        break

            db.write(students)
        else:
            print("Incorrect password format")
        

    def enrol(self):
        if (len(self.student.subjects) < 4):
            id = random.randint(1, 999)
            # self.students.append(Student(id, name, email, password, subjects))
            # db.write(self.students)
            mark = random.randint(25, 100)

            if(mark >= 85):
                grade = "HD"

            elif(75 <= mark < 84):
                grade = "D"

            elif(65 <= mark < 75):
                grade = "C"

            elif(50 <= mark < 65):
                grade = "P"

            else:
                grade = "Z"

            subject = Subject(id, mark, grade)
            
            self.student.subjects.append(subject)

            students = db.read()

            # Find the student in the list by their id or email
            for i, student in enumerate(students):
                if student.id == self.student.id:  # You can use email if needed
                    students[i] = self.student  # Update the student in the list

            db.write(students)

            # self.students.append(Student(id, name, email, password, subjects))
            # db.write(self.students)

            print("Enrolling in Subject-" + str(id))
            print("You are now enrolled in " + str(len(self.student.subjects)) + " out of 4 subjects")

            for subject in self.student.subjects:
                print("[ Subject::" + str(id) + " -- mark =" + str(mark) + " -- grade =  " + grade + " ]")

        else:
            print("Students are allowed to enrol in 4 subjects")

    def remove(self):
        pass

    def show(self):
        if(self.student.subjects is None):
            print("Showing 0 subjects")

        else:
            print("Showing " + str(len(self.student.subjects)) + " subjects")
            for subject in self.student.subjects:
                print(f"[Subject:: id={subject.id} -- mark={subject.mark} -- grade={subject.grade}]")

    def system(self):
        userInput = input("\033[96mStudent Course Menu (c/e/r/s/x): \033[0m")

        while(userInput != "x"):
            match userInput:
                case "c":
                    self.changePassword()
                case "e":
                    self.enrol()
                case "r":
                    pass
                case "s":
                    self.show()
                case _:
                    pass
            userInput = input("\033[96mStudent Course Menu (c/e/r/s/x): \033[0m")