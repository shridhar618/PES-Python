# try and except block
n=int(input("Enter a numerator: "))
try:
    d=int(input("Enter a denominator: "))
    print(f"Result: {n/d}")
except ZeroDivisionError as e:
    print(f"Error: {e}. Denominator cannot be zero.")
except ValueError as e:
    print(f"Error: {e}. Please enter a valid integer for denominator.")
else:
    print("Division performed successfully.")
finally:
    print("Execution completed.")
    
    
try:
    l=[0,2,4,6,8,10]
    i1=int(input("Enter an index to access the list element: "))
    i2=int(input("Enter another index to divide the element: "))
    print(f"Result: {l[i1]/l[i2]}")
except ZeroDivisionError as e:
    print(f"Error: {e}. Division by zero is not allowed.")
except IndexError as e:
    print(f"Error: {e}. Index out of range.")
except ValueError as e: 
    print(f"Error: {e}. Please enter valid integers for indices.")
else:
    print("List access and division performed successfully.")
finally:
    print("Execution completed.")    
    
    

try:
    n=int(input("Enter a number: "))
    assert n%2==0, "The number is not even."
    print(f"You entered an even number: {n}")
except AssertionError as e:     
    print("Not an even number.")
    
else:
    print(n/4)
    
    
finally:
    print("Execution completed.")
    
    
#a program converts user input to integer and handles invalid input such as alphabets or special characters.
try:
    user_input=input("Enter an integer: ")
    converted_input=int(user_input)
    print(f"You entered the integer: {converted_input}")
except ValueError as e:
    print(f"Error: {e}. Please enter a valid integer.") 
    
#a function computes squareroot of number and handle negative input.
import math
def compute_squareroot(num):
    if num<0:
        raise ValueError("Cannot compute squareroot of negative number.")
    return math.sqrt(num)

number=float(input("Enter a number to compute its squareroot: "))
result=compute_squareroot(number)
print(f"The squareroot of {number} is {result}")

#a program performs arithmatic operations on mixed types handle the type errors that are cost by incompatible operations
try:
    a=int(input("Enter an integer: "))
    b=float(input("Enter a float: "))
    print(f"Sum: {a+b}")
    print(f"Difference: {a-b}")
    print(f"Product: {a*b}")
    print(f"Quotient: {a/b}")
except TypeError as e:
    print(f"Error: {e}. Incompatible types for arithmatic operations.")