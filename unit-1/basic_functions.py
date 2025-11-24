x=11
y=2.8
z=1+3j
print(type(x))
print(type(y))
print(type(z))



a=float(x)

b=int(y)

c=complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#type coversion
a=float(x)
b=complex(x)
print(a, b)


c=int(y)
d=complex(y)
print(c, d)


# e=int(z)
# f=(float(z))
# print(e, f)


s1='heloo'
s2="hello"
s3='''hello'''
s4="""hello"""
print(s1, s2, s3, s4)

print(id(s1))
print(id(s2))
print(id(s3))
print(id(s4))


# count()
s1="Hello this statement is used for counting"
c=s1.count('o')
print(c)


c=s1.count('C')
print(c)

#find
s2="Hello, this string is used for implementing the find method"
f=s2.find('o')
print(f)


#index
s3="hello, this string is to implement the index method"
i=s3.index('o')
print(i)

# i=s3.index('O')
# print(i)


#partition
s4="tjis string will be partitioned based on value"
p=s4.partition(' ')
print(p)

p=s4.partition('S')
print(p)

p=s4.partition('P')
print(p)

#split
s5="this string will be split based on value"
s=s5.split(' ')
print(s)

s=s5.split('s')
print(s)


print(len(s5))

# --------------------------
# List
l=[1,2,3,4,5,6,7,8,9]
s=len(l)
print(s)

l1=list("This is a list")
print(l1)

print(type(l1))



l2=l1
print(id(l1))
print(id(l2))


l3=[1,2,3,4]
l4=l3.copy()
print(l3, l4)

l3[2]=45
print(l3, l4)

print(id(l3), id(l4))


l=[1,2,3,4,5,6]
l.append(7)
print(l)

# l.append(8,9,10)

l.extend([8,9,10])
print(l)

#pop() it deletes 4th positioned element
l.pop(4)
print(l)

# l.pop(10)
# print(l)

#remove() it removes element by its name
l.remove(4)
print(l)

#reverse()
l.reverse()
print(l)

#sort()
l.sort()
print(l)


l2=[1,1.5,2+8j,7]


# l2.sort()
# print(l2)

l3=['a','A','apple','Apple']
l3.sort()
print(l3)

# l4=['a',['A'],'Apple']
# l4.sort()
# print(l4)

# l5=[['A'],[1],[9.0],[-9-7j]]
# l5.sort()
# print(l5)


#_________________________________________
#Tuples
t=(1,2,3)
print(type(t))
print(id(t))

t1=(1)
print(type(t1))

t2=tuple('a')
print(type(t2),type(t1))

t3=('a')
print(type(t3))


t4=(3,)
print(type(t4))

t5=((1,2,3),('a','b'),[1,2,3],9,'str')
print(type(t5))
print(type(t5[2]))

#count()
print(t.count(1))

#index()
print(t.index(2))


#____________________________________________________________________________________
#Sets-set is unorder collection of unique items
s={1,2,3}
print(type(s))
print(id(s))

s1={1,1,1,1,2,2,2,3,4,1,2,8,4}
print(s1)
s1.add(1)

s.intersection(s1)
print(s)

print(s1.intersection(s))

print(s1.union(s))

print(s1&s)
print(s1|s)

print(s1-s)
print(s-s1)

print(s.symmetric_difference(s1))
print(s1.symmetric_difference(s))


#frozen_set
l=[1,2,3]
s={1,2,3}
t=(1,2,3)
print(id(l),id(s),id(t))

fl=frozenset(l)
fs=frozenset(s)
ft=frozenset(t)
print(fl,fs,ft)
print(type(fl),type(fs),type(ft))
print(id(fl),id(fs),id(ft))


f_s=frozenset({1,2,3})
print(f_s)

print(f_s.union(fl))

# print(f&f_s)


#___________________________________________________________________________
#Dictinary
d={1:'a'}
print(type(d),id(d))

d['b']='c'
print(d)

#get()
print(d.get('b'))

#items()
print(d.items())

#keys()
print(d.keys())

#values()
print(d.values())

#pop()
print(d.pop())


















