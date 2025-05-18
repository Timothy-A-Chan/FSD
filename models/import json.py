import json
import os
from typing import List, Dict, Any, Tuple

class Student:
    def __init__(self, student_id: str, name: str, score: float):
        self.student_id = student_id
        self.name = name
        self.score = score
        self.passed = score >= 60

    def to_dict(self) -> Dict[str, Any]:
        return {
            "student_id": self.student_id,
            "name": self.name,
            "score": self.score,
            "passed": self.passed
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Student':
        student = cls(data["student_id"], data["name"], data["score"])
        student.passed = data.get("passed", False)
        return student

class StudentManager:
    def __init__(self, filename: str = "students.json"):
        self.filename = filename
        self.students = self._load_students()

    def _load_students(self) -> List[Student]:
        try:
            if not os.path.exists(self.filename):
                return []
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Student.from_dict(student) for student in data]
        except Exception as e:
            print(f"wrong - {str(e)}")
            return []

    def _save_students(self) -> None:
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump([student.to_dict() for student in self.students], file, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error: Unable to save student data - {str(e)}")

    def list_students(self) -> None:
        if not self.students:
            print("The student list is empty")
            return
        print("student list:")
        for student in self.students:
            status = "pass" if student.passed else "fail"
            print(f"  ID: {student.student_id}, Name: {student.name}, Score: {student.score}, State: {status}")

    def group_students_by_score(self) -> None:
        if not self.students:
            print("The student list is empty")
            return
        groups = {
            "Excellent (90-100)": [],
            "Good (80-89)": [],
            "Average (70-79)": [],
            "Pass (60-69)": [],
            "Fail (<60)": []
        }
        for student in self.students:
            if 90 <= student.score <= 100:
                groups["Excellent (90-100)"].append(student)
            elif 80 <= student.score < 90:
                groups["Good (80-89)"].append(student)
            elif 70 <= student.score < 80:
                groups["Average (70-79)"].append(student)
            elif 60 <= student.score < 70:
                groups["Pass (60-69)"].append(student)
            else:
                groups["Fail (<60)"].append(student)
        for group_name, group_students in groups.items():
            if group_students:
                print(f"{group_name}:")
                for student in group_students:
                    print(f"  ID: {student.student_id}, Name: {student.name}, Score: {student.score}")

    def classify_students(self) -> None:
        if not self.students:
            print("The student list is empty")
            return
        passed = [s for s in self.students if s.passed]
        failed = [s for s in self.students if not s.passed]
        print("Students who passed:")
        for student in passed:
            print(f"  ID: {student.student_id}, Name: {student.name}, Score: {student.score}")
        print("Students who failed:")
        for student in failed:
            print(f"  ID: {student.student_id}, Name: {student.name}, Score: {student.score}")

    def delete_student(self, student_id: str) -> None:
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if initial_count == len(self.students):
            print(f"Error: can not find ID is {student_id}")
        else:
            print(f"Deleted student with ID {student_id}")
            self._save_students()

    def clear_all_students(self) -> None:
        if not self.students:
            print("The student list is empty")
            return
        confirm = input("Are you sure you want to delete all student data? This will clear the file.(y/n): ").lower()
        if confirm == 'y':
            self.students = []
            self._save_students()
            print("All student data has been deleted")
        else:
            print("Operation Cancelled")

    def add_student(self, student_id: str, name: str, score: float) -> None:
        if any(s.student_id == student_id for s in self.students):
            print(f"Error: student ID {student_id} has already been used")
            return
        try:
            score = float(score)
            if not (0 <= score <= 100):
                raise ValueError("Score must be between 0 and 100")
        except ValueError as e:
            print(f"Error: Invalid Grade- {str(e)}")
            return
        student = Student(student_id, name, score)
        self.students.append(student)
        self._save_students()
        print(f"Student added: {name} (ID: {student_id})")

def main():
    manager = StudentManager()
    print("welcome to the Student Management System")
    while True:
        print("\n Please select an option :")
        print("1. Check all students")
        print("2. Group students by grades")
        print("3. Divide students into pass/fail")
        print("4. Delete students")
        print("5. Clear all students")
        print("6. Add test data")
        print("7. Exit")
        choice = input("Please enter option 1-7").strip()
        if choice == '1':
            manager.list_students()
        elif choice == '2':
            manager.group_students_by_score()
        elif choice == '3':
            manager.classify_students()
        elif choice == '4':
            student_id = input("Please enter the student you want to delete student ID: ").strip()
            manager.delete_student(student_id)
        elif choice == '5':
            manager.clear_all_students()
        elif choice == '6':
            # Adding test data
            manager.add_student("001", "张三", 85)
            manager.add_student("002", "李四", 59)
            manager.add_student("003", "王五", 92)
            manager.add_student("004", "赵六", 67)
            manager.add_student("005", "孙七", 45)
        elif choice == '7':
            print("Thanks for using the Student Management System")
            break
        else:
            print("Error: Invalid option, please enter a number between 1-7")

if __name__ == "__main__":
    main()    