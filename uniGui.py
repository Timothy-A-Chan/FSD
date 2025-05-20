import tkinter as tk
from tkinter import messagebox, Toplevel
from models.database import Database as db
from controllers.studentSystemController import StudentSystemController
from controllers.subjectSystemController import SubjectSystemController

# Create main root window
root = tk.Tk()
root.title("Login")
root.geometry("300x200")

# Create a controller instance
student_controller = StudentSystemController()

# Authentication function
def authenticate_user(email, password):
    if student_controller.checkEmail(email) and student_controller.checkPassword(password):
        student = student_controller.findStudent(email)
        if student and student_controller.correctLogin(email, password):
            return student
    return None

# Login handler
def handle_login():
    email = email_entry.get()
    password = password_entry.get()
    student = authenticate_user(email, password)

    if student:
        messagebox.showinfo("Login Success", f"Welcome, {email}!")
        open_main_menu(student)
    else:
        messagebox.showerror("Login Failed", "Invalid email, password, or student not found.")

# Main menu window
def open_main_menu(student):
    root.withdraw()
    menu_win = Toplevel(root)
    menu_win.title("Main Menu")
    menu_win.geometry("300x250")

    tk.Button(menu_win, text="Enrolment", width=20, command=lambda: open_enrolment(student)).pack(pady=5)
    tk.Button(menu_win, text="Subject", width=20, command=lambda: open_subject(student)).pack(pady=5)
    tk.Button(menu_win, text="Logout", width=20, command=menu_win.quit).pack(pady=20)

# Enrolment window
def open_enrolment(student):
    enrol_win = Toplevel(root)
    enrol_win.title("Enrolment")
    enrol_win.geometry("300x400")

    subject_system = SubjectSystemController(student, student_controller)

    def enrol_in_subject():
        subject_system.enrol()
        messagebox.showinfo("Success", "Enrolled successfully!")
        enrol_win.destroy()
        open_enrolment(student)

    tk.Button(enrol_win, text="Enroll in a Subject", width=20, command=enrol_in_subject).pack(pady=10)

    tk.Label(enrol_win, text=f"Subjects Enrolled: {len(student.subjects)}").pack(pady=5)

    for subject in student.subjects:
        tk.Label(enrol_win, text=f"Subject ID: {subject.id} - Grade: {subject.grade} - Mark: {subject.mark}").pack(pady=2)

# Subject window (read-only)
def open_subject(student):
    subject_win = Toplevel(root)
    subject_win.title("Subject")
    subject_win.geometry("300x300")

    tk.Label(subject_win, text="Subjects Enrolled:").pack(pady=10)

    for subject in student.subjects:
        tk.Label(subject_win, text=f"Subject ID: {subject.id} - Grade: {subject.grade} - Mark: {subject.mark}").pack(pady=5)

# GUI for login
tk.Label(root, text="Email").pack(pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, width=30, show="*")
password_entry.pack()

tk.Button(root, text="Login", width=20, command=handle_login).pack(pady=20)

# Start GUI loop
root.mainloop()
