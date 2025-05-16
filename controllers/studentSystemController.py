class StudentSystemController:
    
    def system(self):
        userInput = input("\033[96mStudent System (l/r/x): \033[0m")
        while(userInput != "x"):
            match userInput:
                case "l":
                    pass
                case "r":
                    pass
                case "x":
                    pass
                case _:
                    pass
            userInput = input("\033[96mStudent System (l/r/x): \033[0m")