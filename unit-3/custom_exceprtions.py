# class CustomException(Exception):
#     """Raised when the value is less than 18"""
#     pass


# try:
#     age=int(input("Enter your age: "))
#     if age<18:
#         raise CustomException
#     else:
#         print("You are eligible to vote.")
# except CustomException:
#     print("CustomException: Age is less than 18. You are not eligible to vote.")
    
    
    
# class SalaryNotInRange(Exception):
#     '''exception raised when salry is not in the range'''
#     def __init__(self, sal, msg="salary not in (5000,20000) range"):
#         self.sal=sal
#         self.msg=msg
#         super().__init__(self.msg)
        
# try:
#     salary=int(input("Enter your salary: "))
#     if salary<5000 or salary>20000:
#         raise SalaryNotInRange(salary)
#     else:
#         print(f"Your salary is {salary}")
# except SalaryNotInRange as e:
#     print(f"SalaryNotInRange: {e.sal} is invalid. {e.msg}")
    
    
    

# #raising built-in exceptions
# try:
#     x=int(input("Enter the numerator: "))
#     y=int(input("Enter the denominator: "))
#     z=x/y
#     if z>10:
#         raise ValueError(z)
    
# except ValueError:
#     print(f"{z} is outside the given range.")
# else:
#     print(f"{z} is within the given range.")
    
    
    
    
# try:
#     x=int(input("Enter the numerator: "))
#     y=int(input("Enter the denominator: "))
#     z=x/y
#     if y==0:
#         raise ValueError("Denominator cannot be zero.")
    
# except Exception as e:
#     print(f"An error occurred: {e}")
# else:
#     print(f"The result is: {z}")
    
    
#Text file handling
#opening a file
f=open('file1.txt', 'r')

#Attributes of file object
print(type(f))          #prints the type of file object
print(f.name)          #prints the name of the file
print(f.mode)          #prints the mode in which file is opened
print(f.closed)        #prints whether the file is closed or not

#Read the file
str=f.read()
print(str)

#Close the file
f.close()

print(f.closed)        #prints whether the file is closed or not


f=open('file1.txt', 'r')
#Read multiple lines of the file
s=f.readlines()
print(s)
print(type(s))

f.close()


#write a file
with open('file2.txt', 'w') as f1:
    c=f1.write("This is the first line.\n")
    c=f1.write("This is the second line.\n")
    c=f1.write("This is the third line.\n")
    
    print(f"The file is written with {c} number of characters.")
    
    
#write multiple lines to a file
lines=["Line 1: Hello World!\n", "Line 2: Welcome to Python file handling.\n", "Line 3: This is the third line.\n"]

with open('file3.txt', 'w') as f2:
    c=f2.writelines(lines)
    print(f"The file is written with {c} number of characters.")
    
    f2.close()
#append to a file
with open('file3.txt', 'a') as f3:
    c=f3.write("Line 4: This line is appended.\n")
    print(f"The file is appended with {c} number of characters.")
    
    f3.close()