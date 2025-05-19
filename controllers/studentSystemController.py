from models.student import Student
from models.subject import Subject

class StudentSystemController:

    def login(self):
        pass

    def register(self):
        pass
    
    def system(self):
        userInput = input("\033[96mStudent System (l/r/x): \033[0m")
        while(userInput != "x"):
            match userInput:
                case "l":
                    self.login()

                case "r":
                    self.register()

                case "x":
                    pass
                
                case _:
                    pass
            userInput = input("\033[96mStudent System (l/r/x): \033[0m")