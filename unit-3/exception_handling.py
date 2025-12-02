#try and except block
# n=int(input("Enter a numerator: "))
# try:
#     d=int(input("Enter a denominator: "))
#     print(f"Result: {n/d}")
# except ZeroDivisionError as e:
#     print(f"Error: {e}. Denominator cannot be zero.")
# except ValueError as e:
#     print(f"Error: {e}. Please enter a valid integer for denominator.")
# else:
#     print("Division performed successfully.")
# finally:
#     print("Execution completed.")
    
    
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
    
    
