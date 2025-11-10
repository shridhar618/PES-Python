# class Employee:
#     def __init__(self, name, dept, salary):
#         self.name = name
#         self.dept = dept  # Public attribute
#         self.salary = salary  # Private attribute

#     def show(self):
#         print(f"I am {self.name} working in {self.dept} for Rs. {self.salary} salary")

# # Example usage:
# emp = Employee("John Doe", "IT", 50000)
# emp.show()






# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius 
# class Rectangle(Shape):
    
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width
# # Example usage:
# circle = Circle(5)
# rectangle = Rectangle(4, 6)
# print("Area of Circle:", circle.area())
# print("Area of Rectangle:", rectangle.area())
# # Example usage:
# emp = Employee("John Doe", 50000)
# print("Employee Name:", emp.name)  # Accessing public attribute
# print("Employee Salary:", emp.get_salary())  # Accessing private attribute via public method



#use public method to access the data from outside the class
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name  # Public attribute
        self.dept = dept
        self.salary = salary  # Private attribute
        
    

    def show(self):
        print(f"I am {self.name} working in {self.dept} for Rs. {self.salary} salary")

    #protected method to access the data member
    def _display(self):
        print(f"I am {self.name} working in {self.dept} for Rs. {self.salary} salary")
     
    #private method to access the data member   
    def __see(self):
        print(f"I am {self.name} working in {self.dept} for Rs. {self.salary} salary")
        
        
    #private method to access data member
e1=Employee('XYZ', 'IT', 10000)
e1.show()
e1._display()
# e1.__see()


#usage of getter and setter method
class Student:
    def __init__(self, name, age):
        self._name = name       # underscore indicates it's for internal use
        self._age = age

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Name must have at least 2 characters")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value


# Using the class
s = Student("Shridhar", 21)
print(s.name)   # calls getter
print(s.age)

s.name = "Navonmesh"   # calls setter
s.age = 22

print(s.name)
print(s.age)


 
#define a bank account class with attributes name, acc-no and balance. implement 2 methods deposit and withdraw with validations. keep a minimum balance of 500 rs.

#create a product class with attributes name, price and discount. discount is protected. implement a setter that changes price after applying the discount. only if the discount is less than 25%.

#create a car class with a private attributes key. implement the methods accelerate and brake that adjest the limit within the limit of 0-100 km/h.

#create a user class with protected user name and private password admin inherits thge user and adds a private variable called as access level. implement methods to have restricted password access and restricted modification of access level.
    


