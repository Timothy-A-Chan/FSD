from models.student import Student
from models.subject import Subject
import re
from models.database import Database as db
import random
from controllers.subjectSystemController import SubjectSystemController


class StudentSystemController:

    def login(self):
        print("Student Sign In")
        email = input("Email: ")
        password = input("Password: ")

        if(self.checkEmail(email) and self.checkPassword(password)):
            print("email and password formats acceptable")
            if(self.findStudent(email) and self.correctLogin(email, password)):
                subjectSystem = SubjectSystemController(self.findStudent(email), self)
                subjectSystem.system()
                # print("Student " + self.findStudent(email).name + " already exists")
            else:
                print("Student does not exist")

        else:
            print("Incorect email or password format")



    def register(self):
        print("Student Sign Up")
        email = input("Email: ")
        password = input("Password: ")

        if(self.checkEmail(email) and self.checkPassword(password)):

            print("email and password formats acceptable")

            if(self.findStudent(email)):
                print("Student " + self.findStudent(email).name + " already exists")
                return
                
            name = input("Name: ")

            self.students = db.read()  

            id = random.randint(1, 999999)
            # subjects = None
            self.students.append(Student(id, name, email, password))
            db.write(self.students)

            print("Enrolling Student " + name)

        else:
            print("Inccorect email or password format")

        # print("=== All Registered Students ===")
        # for student in self.students:
        #     print(f"ID: {str(student.id).zfill(6)} | Name: {student.name} | Email: {student.email}")


    def checkEmail(self, email):
        pattern = r'^[a-zA-Z]+\.([a-zA-Z]+)@university\.com$'
        return bool(re.match(pattern, email))
    
    def checkPassword(self, password):
        pattern = r'^[A-Z][a-zA-Z]{4,}\d{3,}$'
        return bool(re.match(pattern, password)) 
    
    def findStudent(self, email):
        self.students = db.read()
        for student in self.students:
            if(student.email == email):
                return student
        return None
    
    def correctLogin(self, email, password):
        student = self.findStudent(email)
        if student is not None:
            return student.email == email and student.password == password
        return False
    

    # def courseMenu(self):
    #     userInput = input("Student Course Menu")


    
    def system(self):
        userInput = input("\033[96mStudent System (l/r/x): \033[0m")
        while(userInput != "x"):
            match userInput:
                case "l":
                    self.login()

                case "r":
                    self.register()
                
                case _:
                    pass
            userInput = input("\033[96mStudent System (l/r/x): \033[0m")