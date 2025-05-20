class Student:
    
    def __init__(self, id, name, email, password, subjects = None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.subjects = subjects if subjects is not None else []

