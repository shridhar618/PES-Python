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
class A:
    def __init__(self):
        print('The object initialized')
        
    def __del__(self):
        print('the object is destroyed')
        
a=A()
print(a)
del a 
print(a)
