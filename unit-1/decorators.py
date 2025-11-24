#syntactic decorator
def outer_func(func):
    def inner_func(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
            return func(num1,num2)
    return inner_func

@outer_func
def mult(num1,num2):
    print(num1/num2)
mult(2,3)

#normal decorator

def devide(a,b):
    print(a/b)

def outer_func(func):
    def inner_func(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner_func

devide1=outer_func(devide)
devide1(2,8)