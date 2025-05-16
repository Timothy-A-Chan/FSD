class UniCli:
    
    def main(self):
        userInput = input("University System: (A)dmin, (S)tudent, or X: ")
        while (userInput != "X"):
            match  userInput:
                case "A":
                    print("Admin Mode")
                case "S":
                    print("Student Mode")
                case _:
                    self.help()
        print("Thank You")


if __name__ == "__main__":
    uniCli = UniCli()
    uniCli.main()