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