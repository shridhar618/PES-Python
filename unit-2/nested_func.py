# ------------------------------------------------------
# Example 1: Simple Nested Function
# ------------------------------------------------------

def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()

outer()

# Output:
# Inside outer function
# Inside inner function


# ------------------------------------------------------
# Example 2: Nested Function with Local Variables
# ------------------------------------------------------

def outer():
    x = 10
    print(f'Memory location of x is {id(x)}')
    print(f'x in outer = {x}')

    def inner():
        x = 20
        print(f'Memory location of x in inner is {id(x)}')
        print(f'x in inner = {x}')

    inner()
    print(f'memory location of x in outer is {id(x)}')
    print(f'x in outer = {x}')

outer()

# Output (memory IDs may vary):
# Memory location of x is 9793376
# x in outer = 10
# Memory location of x in inner is 9793696
# x in inner = 20
# memory location of x in outer is 9793376
# x in outer = 10


# ------------------------------------------------------
# Example 3: Passing Arguments to a Nested Function
# ------------------------------------------------------

def outer(n):
    print(f"The value of n in outer is {n}")

    def inner():
        print(f"The value of n in inner is {n}")

    inner()

n = input("Enter a value: ")  # Example input: 5
outer(n)

# Output:
# Enter a value: 5
# The value of n in outer is 5
# The value of n in inner is 5


# ------------------------------------------------------
# Example 4: Modifying 'n' inside Inner Function
# ------------------------------------------------------

def outer(n):
    print(f"The value of n in outer is {n}")

    def inner():
        n = int(input("Enter the number: "))  # Example input: 50
        print(f"The value of n in inner is {n}")

    inner()

n = input("Enter a value: ")  # Example input: 10
outer(n)

# Output:
# Enter a value: 10
# The value of n in outer is 10
# Enter the number: 50
# The value of n in inner is 50


# ------------------------------------------------------
# Example 5: Packing and Unpacking Values (int, float)
# ------------------------------------------------------

(a, b, c) = [1, 2, 3.5]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(type(a), type(b), type(c))

# Output:
# a = 1
# b = 2
# c = 3.5
# <class 'int'> <class 'int'> <class 'float'>


# ------------------------------------------------------
# Example 6: Packing and Unpacking (str, int, complex)
# ------------------------------------------------------

(a, b, c) = ['alpha', 20, 6 + 9j]
print(f'a = {a}')
print(f'b = {b}')
print(f'c = {c}')
print(type(a), type(b), type(c))

# Output:
# a = alpha
# b = 20
# c = (6+9j)
# <class 'str'> <class 'int'> <class 'complex'>


# ------------------------------------------------------
# Example 7: Passing Unpacked Values to Functio
