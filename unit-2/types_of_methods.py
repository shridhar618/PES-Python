class Student:
    school_name = "PES University"     # Class variable

    def __init__(self, name, marks):
        self.name = name               # Instance variable
        self.marks = marks             # Instance variable

    # Instance method
    def show(self):
        print(f"{self.name} scored {self.marks} marks.")

    # Class method
    @classmethod
    def school(cls):
        print("School:", cls.school_name)

    # Static method
    @staticmethod
    def greet():
        print("Welcome to the school portal!")

# Create object
s1 = Student("Shridhar", 95)

# Instance method → needs object
s1.show()

# Class method → can use class or object
Student.school()

# Static method → no self or cls
Student.greet()
