class AdminSystemController:

    def clearDatabase(self):
        pass

    def groupStudents(self):
        pass

    def partitionStudents(self):
        pass

    def removeStudents(self):
        pass

    def show(self):
        pass

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