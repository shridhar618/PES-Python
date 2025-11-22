#-------------------------------------Meta Classes-------------------------------------#

# Creation of the class using type
#1. Define Method
def greet(self):
    print(f'Hello {self.name}')
    
#create a class and attach the method to the class
Student=type('Student', (object,), {'greet': greet, 'name': 'John Doe'})
#Create an instance of the class
s1=Student()
s1.greet()

print(type(s1))

        
#2. Using metaclass to create a class
#Define a metaclass
class Required_id(type):   
    def __new__(cls, name, bases, attrs):
        if 'greet' not in attrs:
            attrs['greet'] = 100
        return super().__new__(cls, name, bases, attrs)
    
#Create a class using the metaclass
class Student(metaclass=Required_id):
    def __init__(self, name):
        self.name = name
        
s1=Student('Alice')
print(s1.name)
print(type(s1))
print(id(s1))
print(s1.greet)  # Accessing the greet attribute added by the metaclass

class Teacher(metaclass=Required_id):
    id=20
    def __init__(self, name):
        self.name = name
        
t1=Teacher('Bob')
print(t1.name)
print(t1.id)
print(t1.greet)  # Accessing the greet attribute added by the metaclass 


#metaclass with inheritance
#create custom metaclass
class CustomMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f'Creating class {name} with CustomMeta')
        attrs['created_by'] = 'CustomMeta'
        attrs['created_on'] = '2024-06-01'
        return super().__new__(cls, name, bases, attrs)
    
# Use metaclass keyword
class Example(metaclass=CustomMeta):
    def greet(self):
        return 'Hello from Example class'
    
#inheriting from a class that uses the custom metaclass
class ExampleB(Example):
    def greet(self):
        print('Hello from ExampleB class')
        
Example().greet()
ExampleB().greet()

#check for the attributes added by the metaclass
print(Example.created_by)
print(Example.created_on)
print(ExampleB.created_by)
print(ExampleB.created_on)


class ExampleC(ExampleB):
    def greet(self):
        print('Hello from ExampleC class')
        
ExampleC().greet()
print(ExampleC.created_by)
print(ExampleC.created_on)

 