class Root:
    def do(self):
        print('Root. do (completed)')
        
#inherited class
class A(Root):
    def do(self):
        print('A.do')
        super().do()
        
class B(A):
    def do(self):
        print('B.do')
        super().do()
        
class C(A):
    def do(self):
        print('C.do')
        super().do()
        
        
class D(B,C):
    pass

class E(C,B):
    pass

D().do()

E().do()


# class F(D,E,B,C):
#     pass

print('MRO of class D:', [cls.__name__ for cls in D.mro()])

print('MRO of class E:', [cls.__name__ for cls in E.mro()])

print(D.__mro__)
print(E.__mro__)



#define a class car with parameter of model and year
# and has method read and update. cretae an electric car that has the attribute battery and has the methods read battery and check battery and also displays how much time bafore the recharge.
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def read(self):
        print(f"Car Model: {self.model}, Year: {self.year}")

    def update(self, model, year):
        self.model = model
        self.year = year
        print("Car details updated!")
        

        


class ElectricCar(Car):
    def __init__(self, model, year, battery):
        super().__init__(model, year)
        self.battery = battery  # in percentage (0–100)

    def read_battery(self):
        print(f"Battery Level: {self.battery}%")

    def check_battery(self):
        if self.battery > 60:
            print("Battery is good. No recharge needed.")
        elif 30 <= self.battery <= 60:
            print("Battery is moderate. Recharge soon.")
        else:
            print("Battery low! Please recharge immediately.")
        time_left = (self.battery / 100) * 5  # assuming 5 hours full charge life
        print(f"Estimated time before recharge: {time_left:.2f} hours")


# Example usage
my_car = ElectricCar("Tesla Model 3", 2023, 45)
my_car.read()
my_car.read_battery()
my_car.check_battery()
my_car.update("Tesla Model Y", 2024)
my_car.read()
    
    
#base class person. child class teacher and student. teaching assitant inherit both teavher and student. each class defines a method called as role.
class Person:
    def role(self):
        print("I am a person.")


class Teacher(Person):
    def role(self):
        print("I am a teacher. I teach students.")


class Student(Person):
    def role(self):
        print("I am a student. I learn from teachers.")


class TeachingAssistant(Teacher, Student):
    def role(self):
        print("I am a teaching assistant. I assist in teaching and also learn.")


# Example usage
p = Person()
t = Teacher()
s = Student()
ta = TeachingAssistant()

p.role()
t.role()
s.role()
ta.role()
