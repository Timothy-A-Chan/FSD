from models.database import Database as db

class AdminSystemController:

    def clearDatabase(self):
        print("Clearing students database")
        confirm = input("Are you sure you want to clear the database (Y)ES/(N)O: ")
        if confirm.strip() == "Y":
            db.write([])  # Overwrite the database with an empty list
            print("Students data cleared")  

    def groupStudents(self):
        students = db.read()

        if not students:
            print("     < Nothing to Display >       ")
            return

        print("Grade Grouping")

        grade_order = {
            "HD": 4,
            "D": 3,
            "C": 2,
            "P": 1,
            "Z": 0,
        }

        # Assign marks and grades to students
        for student in students:
            total = sum(subject.mark for subject in student.subjects)
            average = total / len(student.subjects)
            student.mark = average

            # Assign grade based on average
            if average >= 85:
                student.grade = "HD"
            elif 75 <= average < 85:
                student.grade = "D"
            elif 65 <= average < 75:
                student.grade = "C"
            elif 50 <= average < 65:
                student.grade = "P"
            else:
                student.grade = "Z"

        # Sort by grade (using grade_order mapping)
        students.sort(key=lambda s: grade_order.get(s.grade, -1), reverse=True)
        
        for student in students:
            print(f"{student.grade} --> [{student.name} :: {str(student.id).zfill(6)} --> Grade: {student.mark:.2f}]")

        # Save updated students
        db.write(students)

    def partitionStudents(self):
        print("PASS/FAIL Partition")

        students = db.read()

        if not students:
            print("FAIL --> []")
            print("PASS --> []")
            return

        # Lists to store PASS and FAIL students
        pass_students = []
        fail_students = []

        # Loop through all students to categorize them
        for student in students:
            if student.grade in ["HD", "D", "C", "P"]:
                pass_students.append(student)
            elif student.grade in ["Z", "N/A"]:
                fail_students.append(student)

        # Helper function to safely format mark
        def format_mark(mark):
            return f"{mark:.2f}" if mark is not None else "N/A"

        print("FAIL -->", end=" ")
        for student in fail_students:
            print(f"{student.name} :: {str(student.id).zfill(6)} --> Grade: {student.grade} Mark: {format_mark(student.mark)}", end=" ")
        print()

        print("PASS -->", end=" ")
        for student in pass_students:
            print(f"{student.name} :: {str(student.id).zfill(6)} --> Grade: {student.grade} Mark: {format_mark(student.mark)}", end=" ")
        print()

    def removeStudents(self):
        studentId = input("Remove by ID: ")
        students = db.read()

        # Convert input to integer for comparison
        try:
            studentId = int(studentId)
        except ValueError:
            print("Invalid ID format. Please enter a numeric ID.")
            return

        # Find and remove the student
        student_found = False
        for student in students:
            if student.id == studentId:
                students.remove(student)
                db.write(students)
                print(f"Removing Student {studentId} Account")
                student_found = True
                break

        if not student_found:
            print(f"Student {studentId} does not exist")


    def show(self):
        print("Student List")
        students = db.read()
        if not students:
            print("     < Nothing to Display >       ")

        else:
            for student in students:
                print(student.name + " :: " + str(student.id) + " --> Email: " + student.email)

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