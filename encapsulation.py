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
e1.__see()
    
    


