from models.admin import Admin
from models.student import Student
from controllers.adminSystemController import AdminSystemController
from controllers.studentSystemController import StudentSystemController
from models.database import Database as db


class UniCli:

    def __init__(self):
        db.initialize()
        self.students = db.read() 

    def main(self):
        userInput = input("\033[96mUniversity System: (A)dmin, (S)tudent, or X: \033[0m")
        while (userInput != "X"):
            match  userInput:
                case "A":
                    adminSystem = AdminSystemController()
                    adminSystem.system()
                case "S":
                    studentSystem = StudentSystemController()
                    studentSystem.system()
                case _:
                    pass
            userInput = input("\033[96mUniversity System: (A)dmin, (S)tudent, or X: \033[0m")
        print("\033[93mThank You\033[0m")


if __name__ == "__main__":
    uniCli = UniCli()
    uniCli.main()