class Student:
    
    def __init__(self, id, name, email, password, subjects = None, grade = None, mark = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects is not None else []
        self.grade = grade
        self.mark = mark

