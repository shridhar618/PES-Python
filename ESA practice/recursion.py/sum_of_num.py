def sn(num):
    if num==0:
        return 0
    
    return num+sn(num-1)

num=5
result=sn(num)
print(result)