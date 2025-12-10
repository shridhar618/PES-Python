#-------------------------------------------1.Encapsulation---------------------------------------------
#Encapsulation is the bundling of data and methods that operate on that data within a single

#use public method to access the data from outside the class
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name      # Public attribute
        self._dept = dept      # Protected attribute
        self.__salary = salary  # Private attribute (note the double underscore)

    # Public method
    def show(self):
        print(f"I am {self.name} working in {self.dept} for Rs. {self.__salary} salary")

    # Protected method
    def _display(self):
        print(f"[Protected] I am {self.name} working in {self.dept} for Rs. {self.__salary} salary")

    # Private method
    def __see(self):
        print(f"[Private] I am {self.name} working in {self.dept} for Rs. {self.__salary} salary")

    # Public method to access private method
    def access_private(self):
        self.__see()  # Calling the private method inside a public one


# Create object
e1 = Employee('XYZ', 'IT', 10000)

# Access public method
e1.show()

# Access protected method (possible, but not recommended)
e1._display()

# Access private method (NOT allowed directly)
# e1.__see()   ❌  This will cause an AttributeError

# Access private method through a public method
e1.access_private()  #✅



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
    


