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

#--------------------reduce function---------------------
from functools import reduce
l=reduce(lambda a,b:a+b, [1,2,3,4,5,6,7,8,9,10])
print(l)

#---------------------zip function------------------------
print(list(zip([1,2,3,4,5],['a','b','c','d','e'])))
print(list(zip([1,2,3,4,5,6,7,8,9],['a','b','c','d','e'])))

# -----------------------max()---------------------------
print(max('a','A','aa','AA'))
print((max([1,2,3,4],[1,2,3,4],[1,2,4,5],[1,2,6])))

#------------------------min()---------------------------
print(min('a','A','aa','AA'))
print((min([1,2,3,4],[1,2,3,4],[1,2,4,5],[1,2,6])))



#---------------------list comprehension-------------------
l=[a for a in range(20)]
print(l)

l=[a*2 for a in range(20) if a%2==0]
print(l)

l=


#-------------------conditional comprehension--------------------
l=[a*2 if a%2==0 else a+3 for a in range(20)]
print(l)

#---------------------nested comprehension----------------------
l=[a*b for a in range(1,5) for b in range(1,3)]
print(l)

#nested comprehension with condition
l=[a*b for a in range(1,10) for b in range(1,5) if (a+b)%2==0 ]
print(l)

#set comprehension
s={a for a in range(20)}
print(s)

#conditional set comprehension
s={a for a in range(20) if a%2==0}
print(s)

#nested set comprehension
s={a+b for a in range(1,5) for b in range(1,5)}
print(s)

#nested conditional comprehension
s={(a,b) for a in [1,2,3,4] for b in [4,5] if (a+b)%2==0}
print(s)

#dictionary comprehension
d={a:a*a for a in range(1,6)}
print(d)

#conditional dictionary comprehension
d={a:a*a for a in range(1,11) if a%2==0}
print(d)

#nested dictionary comprehension
d={a:{b:b*b for b in range(1,4)} for a in range(1,4)}
print(d)

#nested conditional dictionary comprehension
d={a:{b:b*b for b in range(1,6) if b%2==0} for a in range(1,6) if a%2!=0}
print(d)



