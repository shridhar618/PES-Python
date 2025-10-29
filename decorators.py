#Wrapper Function
def wrap(f):
    def inner():
        print("Got decorated")
        f()
    
    return inner

#Normal Function
def func():
    print("This is an ordinary output")
    
#Decorate the normal function with the wrapper function
df=wrap(func)
print(type(df))

df()

#Decorators for functions that have parameters
#Normal Function
def div(x,y):
    print(x/y)
    
#Wrapper Function
def check(f):
    def value(x,y):
        if x<y:
            x,y=y,x
            return f(x,y)
    return value

df=check(div)
df(10,12)

#Syntatic Decoration
def Split_val(f):
    def val():
        func=f()
        s_s=func.split()
        return s_s
    return val

def upper_val(f):
    def val():
        func=f()
        u_v=func.upper()
        return u_v
    return val

@upper_val
def input_val():
    return 'This is Python Program'

print(input_val())

@Split_val
def input_val():
    return 'This is Python Program'
print(input_val())



#Wrapper Function
def dec(f):
    def wrap(*args, **kwargs):
        print(f'The position arguments are {args}')
        print(f'the keyword argumenets are {kwargs}')
        f(*args)
    return wrap

@dec
def func_no():
    print("no arguments passed")
func_no()

@dec
def f_pos(a,b,c):
    print(f'the arguments passed are {a}, {b}, {c}')
    
f_pos(1,2,3)

#apply the decorator on a func. that takes keyword arguments
@dec
def f_key():
    print('The function takes keyword Arguments')
f_key(f_name='Harry', l_name='Potter', age=11)


#use an iterator to print the keys in dictionary
my_dict = {'name': 'Shridhar', 'age': 21, 'city': 'Mangalore'}

key_iter = iter(my_dict)

print("Keys in dictionary:")
for key in key_iter:
    print(key)

#use an iterators to print the value of iterator
my_dict = {'name': 'Shridhar', 'age': 21, 'city': 'Mangalore'}

value_iter = iter(my_dict.values())

print("Values in dictionary:")
for value in value_iter:
    print(value)

#define user def func reverse. that, iterates over the in the reverse orderand prints the output
def reverse(data):
    print("Reversed output:")
    for item in reversed(data):
        print(item)

reverse([10, 20, 30, 40])

#write a decorator called green that adds hello to the original func that prints the user name
def green(func):
    def wrapper(name):
        print("Hello", end=" ")
        func(name)
    return wrapper

@green
def show_name(name):
    print(name)

show_name("Shridhar")

#create a decorator that prints func execution started and func execution ended before and after the wrap function executes
def logger(func):
    def wrapper(*args, **kwargs):
        print("Function execution started")
        result = func(*args, **kwargs)
        print("Function execution ended")
        return result
    return wrapper

@logger
def greet():
    print("Welcome to Python programming!")

greet()

#apply a decorator to the recursive func of factorial and prints how manyn time the func was called
def count_calls(func):
    count = 0
    def wrapper(n):
        nonlocal count
        count += 1
        print(f"Function called {count} times")
        return func(n)
    return wrapper

@count_calls
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial:", factorial(5))

