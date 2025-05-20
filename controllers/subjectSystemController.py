from models.subject import Subject

class SubjectSystemController:

    def change(self):
        pass

    def enrol(self):
        pass

    def remove(self):
        pass

    def show(self):
        pass

    def system(self):
        userInput = input("\033[96mStudent Course Menu (c/e/r/s/x): \033[0m")

        while(userInput != "x"):
            match userInput:
                case "c":
                    pass
                case "e":
                    pass
                case "r":
                    pass
                case "s":
                    pass
                case _:
                    pass
            userInput = input("\033[96mStudent Course Menu (c/e/r/s/x): \033[0m")