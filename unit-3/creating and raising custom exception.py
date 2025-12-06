class CustomException(Exception):
    """Raised when the value is less than 18"""
    pass


try:
    age=int(input("Enter your age: "))
    if age<18:
        raise CustomException
    else:
        print("You are eligible to vote.")
except CustomException:
    print("CustomException: Age is less than 18. You are not eligible to vote.")
    
    
    
class SalaryNotInRange(Exception):
    '''exception raised when salry is not in the range'''
    def __init__(self, sal, msg="salary not in (5000,20000) range"):
        self.sal=sal
        self.msg=msg
        super().__init__(self.msg)
        
try:
    salary=int(input("Enter your salary: "))
    if salary<5000 or salary>20000:
        raise SalaryNotInRange(salary)
    else:
        print(f"Your salary is {salary}")
except SalaryNotInRange as e:
    print(f"SalaryNotInRange: {e.sal} is invalid. {e.msg}")
    
    
    

#raising built-in exceptions
try:
    x=int(input("Enter the numerator: "))
    y=int(input("Enter the denominator: "))
    z=x/y
    if z>10:
        raise ValueError(z)
    
except ValueError:
    print(f"{z} is outside the given range.")
else:
    print(f"{z} is within the given range.")
    
    
    
    
try:
    x=int(input("Enter the numerator: "))
    y=int(input("Enter the denominator: "))
    z=x/y
    if y==0:
        raise ValueError("Denominator cannot be zero.")
    
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"The result is: {z}")
    
    
