#constructor
class Coding:
    def __init__(self):
        print("The object has been initialized")
        
    def show(self):
        print("the object has been shown")
        
        
Coding()
Coding().show()

# #parameterized constructor
# class Addition:
#     def __init__(self):
#         self.f=f
#         self.s=s
#     def Calculate(self):
#         self.ans=self.f+self.s
#     def Display(self):
#         print(f"The addition of {self.f} and {self.s} results in {self.ans}")


# a=Addition(10,20)
# a.Calculate()   

# a.Display()     


# class A:
#     def init(self):
#         print('the object has been created')
        
# a=A()
# print(a)

# del a
# print(a)

#destructor
# class A:
#     def __init__(self):
#         print('The object initialized')
        
#     def __del__(self):
#         print('the object is destroyed')
        
# a=A()
# print(a)
# a.__del__()
# print(a)


#static and class method

#1.static method
class NewClass:
    val=10
    def __init__(self,value):
        self.value=value
    @staticmethod
    def count():
        NewClass.val+=1
    def show(self):
        print(f'the number of objects created is {NewClass.val}')

o=NewClass(10)
o.count()

o.show()

NewClass(10).count()
NewClass(10).show()

#2.class methods
class NewClass:
    val=10
    def __init__(self,a,b):
        self.a=a
        self.b=b
    @classmethod
    def incr(cls,x):
        cls.val+=1
    def show(self):
        print(f'the attribute is {self.a}, {self.b}, the val is {NewClass.val}')

o=NewClass(10,3)
o.incr(10)

o.show()

o1=NewClass('hello', 'python')
o1.incr(25)

o1.show()

# NewClass(10).count()
# NewClass(10).show()


#new() method
class NewClass:
    def __new__(cls, a):
        print('Inside new method')
        i=super().__new__(cls)  # super refers to the parent class which is the inbuilt object class
        return i
    def __init__(self, b):
        print('inside init method')
        self.b=b
    def show(self):
        print(f'the stored value is {self.b}')
        
        

o=NewClass(10)
o.show()

#super()
class NewClass:
    def __new__(cls, *a):
        print('Inside new method')
        i=super().__new__(cls)
        return i
    def __init__(self):
        print('Inside init method')
        
o=NewClass()



#class variable and instance variable
class Student:
    school_name='PES Unversity'
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def show(self):
        print(f'the student {self.name} of{self.age} years is studying in {self.school_name}')
        print(f'the student {self.name} of{self.age} years is studying in {Student.school_name}')
        
s1=Student('ABC', 20)
s2=Student('PQR', 18)
s3=Student('ABC', 20)
s4=Student('XYZ', 19)

s1.show()


#Modify class variable
s1.school_name='PESU'
s1.show()

s1.age= 21
s1.show()
s2.show()
s3.show()
s4.show()

Student.adress='RR Campus'

print(s1.school_name,s1.adress)

s1.fname='PQR'
s3.fname='XYZ'

print(s1.name, s1.age, s1.fname)
print(s3.name, s3.age, s3.fname)
# print(s2.name, s2.age, s2.fname)

#composition
#laptop has processor, battery, screen, keyboard
class Processor:
    def __init__(self, brand, cores):
        self.brand=brand
        self.cores=cores
    def process(self):
        print(f'process running with {self.cors} cores of {self.brand}')
        
class Battery:
    def __init__(self, capacity):
        self.capacity=capacity
    def charge(self):
        print(f'battery charging with capacity {self.capacity} mAH')
        
class Screen:
    def __init__(self, size):
        self.size=size
    def display(self, content):
        print(f'displaying {content} on {self.size} inched screen') # here, content is not an attribute of the screen. it cannot be reffered through self.

class Keyboard:
    def __init__(self, category):
        self.category=category
    def typed_key(self,key):
        print(f'{key} is pressed on {self.category} keyboard') # key is not an attribute of the keyboard. it cannot be reffered through self.
        
class Laptop:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
        # create component objects
        self.processor=Processor('Intel i7', 8)
        self.battery=Battery(6000)
        self.keyboard=Keyboard('Backlit')
        
    def turn_on(self):
        print(f'{self.model} of {self.brand} is turned on!!!')
        self.processor.process()
        
    def show_content(self, message):
        self.screen.display(message)
        
    def charge_laptop(self):
        self.battery.charge()
        
    def use_keyboard(self, key):
        self.keyboard.typed_key(key)
        
l1=Laptop('Dell', 'Inspiron 15')
l1.turn_on()
        
l1.show_content('Welcome, Enjoy New Laptop')

l1.use_keyboard('Tab')
l1.charge_laptop()


#chess game is played with the board and pieces that are pawns, rooks, bishop,king,queen....

class Piece:
    def __init__(self, color):
        self.color=color
        
#pawn is the typoe of piece
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type='pawn'
        
#board has 8 pawns of each color.will have 1 king,queen of each color.
# class Board:
#     def __init__(self):
#         self.grid=[[None for _ in range(8)] for _ in range(8)]
#     def init_board(self):
#         #create pawns to be placed on second and last but second row.
#         self.grid[1]=[Pawn('White') for _ in range(8)]
#         self.grid[6]=[Pawn('Black') for _ in range(8)]
#     def print_board(self):
#         for row in self.grid:
#             print([piece.type if piece else '___' for piece in ])



# class GameL:
            


