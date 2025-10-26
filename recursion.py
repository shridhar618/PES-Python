# #Recursion to find the sum of first n natural numbers
# def snn(n):
    
#     if n==0:
#         return 0
#     else:
#         return n + snn(n-1)
    
# n=int(input("Enter a number: "))
# print(f"The sum of first {n} natural numbers is {snn(n)}")


# #Recursion to find factorial of a number
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fact(n-1)
    
# n=int(input("Enter a number: "))
# print(f"The factorial of {n} is {fact(n)}")


# #Recursion to find nth Fibonacci number
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# n=int(input("Enter a number: "))
# print(f"The {n}th Fibonacci number is {fib(n)}")

# #Recursion to find GCD of two numbers
# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b, a % b)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(f"The GCD of {a} and {b} is {gcd(a,b)}")


# #Recursion to find LCM of two numbers
# def lcm(a,b):
#     def gcd(a,b):
#         if b==0:
#             return a
#         else:
#             return gcd(b, a % b)
#     return abs(a*b) // gcd(a,b)

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# print(f"The LCM of {a} and {b} is {lcm(a,b)}")

# #Recursion to reverse a string
# def reverse_string(s):
#     if s == "":
#         return s
#     else:
#         return s[-1] + reverse_string(s[:-1])

# s = input("Enter a string: ")
# print(f"The reverse of '{s}' is '{reverse_string(s)}'")


# #Recursion for adding upto n values
# def sumof(n):
#     if n==0:
#         return 0
#     else:
#         return n + sumof(n-1)

# n=int(input("Enter a number: "))
# print(f"The sum of first {n} natural numbers is {sumof(n)}")


#Recursion to find palindrome
# def is_palindrome(s):
#     if len(s) <= 1:
#         return True
#     else:
#         if s[0] == s[-1]:
#             return is_palindrome(s[1:-1])
#         else:
#             return False

# s = input("Enter a string: ")
# if is_palindrome(s):
#     print(f"'{s}' is a palindrome.")
# else:
#     print(f"'{s}' is not a palindrome.")



#___________________________________________________________________________________________________________
#Anonymous function
f=lambda x:x**2
print(f(10))


l=[1,4,7,9,-9,67.8]
#map function to square each element
x=map(lambda x:x**2,l)
print(list(x))

#map function to find length of each string
d=list(map(len,['apple', 'banana', 'cherry', 'date']))
print(d)


def square(n):
    return n**2
sq=list(map(square, [1,2,3,4,5,6,7,8,9]))
print(sq)

#filter function
c=[10,25,30,45,50,60]
d=list(filter(lambda x:x%2==0,c))
print(d)


#Lambda functions condition based 
is_even=lambda x: x%2==0
print(is_even(10))

l=list(map(is_even, [10,11,23,56,82,90]))
print(l)