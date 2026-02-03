def gcd(a,b):
    if b==0:
        return a
    return gcd(a,b%a)

a=10
b=20¸
result=gcd(a,b)
print(result)