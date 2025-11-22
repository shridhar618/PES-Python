def outer():
    print("Inside outer function")
    def inner():
        print("Inside inner function")
    inner()
outer()


def outer():
    x=10
    print(f'Memory location of x is {id(x)}')
    print(f'x in outer={x}')
    def inner():
        x=20
        print(f'Memory location of x in inner  is {id(x)}')
        print(f'x in inner={x}')
    inner()
    print(f'memory location of x in outer is {id(x)}')
    print(f'x in outer ={x}')
outer()


#passing arguments to nested function
def outer(n):
    print(f"the value of n in outer is {n}")
    def inner():
        print(f"the value of n in inner is {n}")
    inner()

n=input("Enter a value:")
outer(n)


#modifying n in input
def outer(n):
    print(f"the value of n in outer is {n}")
    def inner():
        n=int(input("Enter the number:"))
        print(f"the value of n in inner is {n}")
    inner()
n=input("Enter a value:")
outer(n)


#packing and unpacking of values
(a,b,c)=[1,2,3.5]
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')

print(type(a),type(b),type(c))


(a,b,c)=['alpha', 20, 6+9j]
print(f'a={a}')
print(f'b={b}')
print(f'c={c}')
print(type(a),type(b),type(c))

# def unpack():
#     a,b,c=[1,2,3]
#     print(f'a={a}')
#     print(f'b={b}')
#     print(f'c={c}')
#     print(type(a),type(b),type(c))
# a,b,c=[1,2,3]
# unpack(a,b,c)


