# def rev(str):
#     rev=""
#     for i in str:
#         rev=i+rev
#     return rev

# str=input("enter a string:")
# result=rev(str)
# print(result)

# def rev_str(str):
#     if str=="":
#         return str
#     return rev_str(str[1:])+str[0]

# str="shridhar"
# print(rev_str(str))
        
        
def rev(str):
    if str=="":
        return str
    return rev(str[1:])+str[0]

str="shridhar"
result=rev(str)
print(result)
    