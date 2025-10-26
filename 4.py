from collections import OrderedDict

n=int(input("Enter number of integers:"))

print("Enter the integers:")
numbers=[]
for i in range(n):
    num=int(input(f"numbers {i+1}: "))
    numbers.append(num)
    
unique_numbers=OrderedDict()

for num in numbers:
    if num not in unique_numbers:
        unique_numbers[num]=True
        
print("\n Unique numbers in the same order:")
for num in unique_numbers.keys():
    print(num, end="")