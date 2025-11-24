class Employee:
    def __init__(self, name, dept, salary):
        self.name = name            # Public attribute
        self._dept = dept           # Protected attribute
        self.__salary = salary      # Private attribute

    # Public method
    def show(self):
        print(f"I am {self.name} working in {self._self_dept()} department for Rs. {self.__salary} salary")

    # Protected method
    def _display(self):
        print(f"[Protected] Name: {self.name}, Department: {self._dept}, Salary: {self.__salary}")

    # Private method
    def __see(self):
        print(f"[Private] I am {self.name} working in {self._dept} for Rs. {self.__salary} salary")

    # Public method to access private method
    def access_private(self):
        self.__see()

    # Protected method to access the protected variable
    def _self_dept(self):
        return self._dept
        

# Create an object
e1 = Employee('XYZ', 'IT', 10000)

# Access public method
e1.show()

# Access protected variable (possible, but not recommended)
print("Accessing protected variable directly:", e1._dept)

# Access protected method
e1._display()

# Access private method through public method
e1.access_private()

# Trying to access private variable directly → ERROR
# print(e1.__salary)   ❌




#.    For Refference
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name          # Public attribute
        self._dept = dept         # Protected attribute
        self.__salary = salary    # Private attribute

    # 1️⃣ Public Method
    def show(self):
        print(f"[Public] I am {self.name} working in {self._dept} for Rs. {self.__salary} salary")

    # 2️⃣ Protected Method
    def _display(self):
        print(f"[Protected] I am {self.name} working in {self._dept} for Rs. {self.__salary} salary")

    # 3️⃣ Private Method
    def __see(self):
        print(f"[Private] I am {self.name} working in {self._dept} for Rs. {self.__salary} salary")

