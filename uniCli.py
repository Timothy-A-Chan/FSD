from models.admin import Admin
from models.student import Student

class UniCli:
    
    def main(self):
        userInput = input("\033[96mUniversity System: (A)dmin, (S)tudent, or X: \033[0m")
        while (userInput != "X"):
            match  userInput:
                case "A":
                    admin = Admin()
                    admin.system()
                case "S":
                    student = Student()
                    student.system()
                case _:
                    pass
            userInput = input("\033[96mUniversity System: (A)dmin, (S)tudent, or X: \033[0m")
        print("\033[93mThank You\033[0m")


if __name__ == "__main__":
    uniCli = UniCli()
    uniCli.main()