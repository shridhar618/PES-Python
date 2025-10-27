def is_even(n):
    if n%2==0:
        return n
    
l=list(filter(is_even, range(20)))
print(l)


def is_even(n):
    if n%2==0:
        return n
    
l=list(filter(lambda x: x%2==0, range(20)))
print(l)

#reduce function
from functools import reduce
l=reduce(lambda a,b:a+b, [1,2,3,4,5,6,7,8,9,10])
print(l)

#zip function
print(list(zip([1,2,3,4,5],['a','b','c','d','e'])))

print(list(zip([1,2,3,4,5,6,7,8,9],['a','b','c','d','e'])))


