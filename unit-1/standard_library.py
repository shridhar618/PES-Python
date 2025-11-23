import sys
# print(f"the python version is {sys.version}")
# print(f"the operating system is {sys.platform}")
# print('Enter user name')
# u_name=sys.stdin.readline().rstrip('\n')
# #equivalent to input()
# sys.stdout.write(u_name+'\n\n')
# #equivalent to print(u_name);print('\n)
# sys.stderr.write('this is a error message')

n=123567890
l=[1,2,3,4,5,6,7,8,9,0]
l1=['1','2','3','4','5','6','7','8','9','0']
s={1,2,3,4,5,6,7,8,9,0}
s1={'1','2','3','4','5','6','7','8','9','0'}
t=(1,2,3,4,5,6,7,8,9,0)
t1=('1','2','3','4','5','6','7','8','9','0')
d={'1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0'}
d1={1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}
# d2={}
# d3={}

print(f"the size of {n} is {sys.getsizeof(n)} bytes")
print(f"the size of {l} is {sys.getsizeof(l)} bytes")
print(f"the size of {s} is {sys.getsizeof(s)} bytes")
print(f"the size of {s1} is {sys.getsizeof(s1)} bytes")
print(f"the size of {t} is {sys.getsizeof(t)} bytes")
print(f"the size of {t1} is {sys.getsizeof(t1)} bytes")
print(f"the size of {d} is {sys.getsizeof(d)} bytes")
print(f"the size of {d1} is {sys.getsizeof(d1)} bytes")

# sys.exit(0)

# print(f"the size of {l} is {sys.getsizeof(1)} bytes")



#__________________________________________counter___________________________________________________________________
from collections import Counter
l=[1,2,3,4,5]
print(Counter(l))

s="this is the statement"
print(Counter(s))



#--------------------------------------Deque()---------------------------------------------
from collections import deque
d=deque([10,20,30,40])
print(type(d))
print(d)

#insertion in deque
# ________rear_________
d.append(60)
print(d)

#_______front__________
d.appendleft(70)
print(d)

#Deletion
#________rear________
d.pop()
print(d)

#_______front_______
d.popleft()
print(d)


#-----------------------------chainmap------------------------------------

from collections import ChainMap as cm
d={1:'a',2:'b'}
d1={2:'c',3:'d'}
d2={4:'e',3:'f'}

c=cm(d,d1,d2)
print(c)
print(type(c))

print(c[1])
print(c[4])
print(c[2])

#Adding a new chain at front of a chainmap
print(id(c))

c.new_child({4:'g',6:'h',7:'i'})
print(c)
print(id(c))

#View all maps except the first map
print(c.parents)

print(c.items())
print(c.keys())
print(c.values())



#Ordered Dictionary
from collections import OrderedDict as od
#create
o_d=od({1:'a',2:'b',2:'c',3:'d'})
print(type(o_d))

o_d1=od([(1,'a'),(2,'b')])
print(type(o_d1))

#Move values
o_d.move_to_end(1)
print(o_d)

#display in reverse order
for k in o_d:
    print(k)

for i in reversed(o_d):
    print(i)

#default dictionary
d={1:'a',2:'b'}
print(type(d))
print(d[1],d[2])

#Integer default dictionary
from collections import defaultdict as dd
id=dd(int)
id['a']=1
id['b']+=1
print(id, type(id), id['c'])

#complex default dictionary
id=dd(complex)
id['a']=1
id['b']+=1
print(id, type(id), id['c'])


id=dd(float)
id['a']=1
id['b']+=1
print(id, type(id), id['c'])

# id=dd(dict)
# id['a']=1
# id['b']+=1
# print(id, type(id), id['c'])

# id=dd(tuple)
# id['a']=1
# id['b']+=1
# print(id, type(id), id['c'])


# id=dd(set)
# id['a']=1
# id['b']+=1
# print(id, type(id), id['c'])


#function default dictionary
def valuenotpresent():
    return 'Value has not been created'

id=dd(valuenotpresent)
id['a']=1
id['b']=1
print(id, type(id), id['c'])   

students=[{'name': 'shridhar', 'score': 23},
          {'name': 'shridhar', 'score': 67},
          {'name': 'shridhar', 'score': 80}
          ]

print(students)



# #creation of user dictionary
# class MyUserDict(MyUserDict):
#     def get_keys(self):
#         return [keys.upper() for keys in self.keys()]
    
# cd= MyUserDict({'apple':10,'banana':20,'cherry':30})

#----------------------------------named tuple------------------------------------
from collections import namedtuple
Person=namedtuple('person',['name','age'])
p1=Person(name='Albus', age=120)
p2=Person('Bathilda', 70)
p3=Person(age=11, name='Harry')

print(p1)
print(p3.name)
print(p2)

#user list
from collections import UserList
class CustomList(UserList):
    def addtwice(self, value):
        self.data.append(value)
        self.data.append(value)
    def remtwice(self, pos):
        self.data.pop(pos)
        self.data.pop(pos)

#create instance of custom list
c1=CustomList([1,2,3,4,5,6,7])
c1.append(8)
print(c1)

c1.extend([9,10])
print(c1)

c1.insert(0,10)
print(c1)

c1.remove(4)
print(c1)

c1.reverse()
print(c1)

c1.sort()
print(c1)

c1.addtwice(12)
print(c1)

c1.remtwice(5)
print(c1)

#--------------------------------------user string-----------------------------
from collections import UserString
#create custom string
class MyString(UserString):
    def uppercon(self):
        return self.upper()
    def add_exclamation(self):
        return self.data+'!!!'
    
#create an instance of custom string
cs=MyString("hello, how are you")
print(cs)

#Custom Methods
print(cs.uppercon())
# print(id(cs))

print(cs.add_exclamation())



#function definition
def add(a, b):
    'This function adds a to b'
    return a+b

c=add(10, 20)
print(c)

d=add(34.0, 32)
print(d)

e=(23+9j, 10)
print(e)

f=(90-89j)
print(f)

g=add('apple','banana')
print(g)

h=add([1,2,3],[4,5,6])
print(h)


#Required parameter
# add(10)

#keyword argument
i=add(b=89, a=90)
print(i)

#default argument
f=add(40, 50)
print(f)

#variable length argument
def add(*n):
    sum=0
    for i in n:
        sum=sum+i
    return sum

print(add())

print(add(10,20,30,40,50))

#variable with required/keyword/default
def add(*n, a=10, b=30):
    sum=0
    for i in n:
        sum=sum+i
    sum=sum+a
    sum=sum+b
    return sum

print(add(a=20,b=30))
print(add(10,20,30))

l=[1,2,3,4]

def list_mod(l):
    l.append(20)
    l.append(30)
    print(l)
    return

print(list_mod(l))


# def con(a,b):
#     a+=b
#     return a 

# a="hello", b="world"
# print(con(a,b))
# print(id(a), id(b))

 