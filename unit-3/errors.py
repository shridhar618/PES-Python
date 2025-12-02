# #syntax error 
# x=10
# if x==10
# print(x)  



# x=10
# if x==10:
# print(x) #indentation error



# def fact_cal(n):
#     r=1
#     for i in range(n):
#         r=r*i
#     print(r)
    
# fact_cal(3)
# #logical error. because loop starts with 0.


#List of exceptions handled in python
import builtins
l=[name for name in dir(builtins) if isinstance(getattr(builtins, name), type) and issubclass(getattr(builtins, name), BaseException)]
print("List of exceptions in python:")
for exception in l:
    print(exception)
    
#Arithmatic Error
#a. floating point error
if 1.2-1.0==0.2:
    print("Equal")
else:
    print("Not Equal")
    
#b. Overflow error
# import math
# math.exp(1000)


def fact_cal(n):
    r=1
    for i in range(1,n+1):
        r=r*i
    return r
print(fact_cal(1000))



#zero division error
# x=10/0
# print(x)

#Index error
# l=[1,2,3]
# print(l[5])

#key error
# d={'a':1, 'b':2}
# print(d['c'])

#attribute error
# s="hello to errors"
# s.reverse()
# print(s)

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old.')
        
p1=Person("Alice", 30)
# p1.talk()


#assesrsion error
# age=-5
# assert age>=0, "Age cannot be negative"

def divide_numbers(a, b):
    assert b!=0
    return a/b
print(divide_numbers(10,2))
# print(divide_numbers(10,0))


#fileExists error
# def create_file(file_path):
#     open(file_path, 'x')#creates a flie if not exists
#     print(f'File {file_path} created successfully.')
    
# create_file('testfile.txt')


# #file not found error
# f=open('non_existent_file.txt', 'r')#r opens the file if it exists in read mode
# print("File opened successfully.")


#IO error
try:
    f=open('testfile.txt', 'r')
    print("File opened successfully.")
    
except IOError as e:
    print(f"IOError: {e}")
    
    
#Key error
# d={'a':1, 'b':2}
# d['adress']

#Lookup error
try:
    d={'a':1, 'b':2}
    print(d['c'])
except LookupError as e:
    print(f"LookupError: {e}")
    
    
# x='10'
# y=10
# z=x+y  #Type error
# print(z)


# index error
# l=[1,2,3]
# print(l[3])


#value error
# v=int("hello")
# print(v)


#Keyboard interrupt error
# name=input("Enter the value")


#unbound local error 
def fact_cal(n):
    for i in range(1,n+1):
        r=r*i
    return r

print(fact_cal(5))





