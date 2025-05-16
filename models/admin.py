class Admin:

    def system(self):
        userInput = input("\033[96mAdmin System (c/g/p/r/s/x): \033[0m")

        while(userInput != "x"):
            match userInput:
                case "c":
                    pass
                case "g":
                    pass
                case "r":
                    pass
                case "s":
                    pass
                case _:
                    pass
            userInput = input("\033[96mAdmin System (c/g/p/r/s/x): \033[0m")