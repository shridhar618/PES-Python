def rev(str):
    rev=""
    for i in str:
        rev=i+rev
    return rev

str=input("enter a string:")
result=rev(str)
print(result)
        
    