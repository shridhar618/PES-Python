def find_max_and_min(numbers):
    numbers1=sorted(numbers)
    max=numbers1[-1]
    min=numbers1[0]
    print(max)
    print(min)

numbers=[1,5,3,2,8,7,9]
result=find_max_and_min(numbers)
print(result)
    