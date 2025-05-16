class SubjectSystemController:

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