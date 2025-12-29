import pickle as p

# numeric datatypes
a = 10
b = 10.5
c = 10 - 9j

with open('numeric.pkl', 'wb') as f:
    p.dump(a, f)
    p.dump(b, f)
    p.dump(c, f)

with open('numeric.pkl', 'rb') as f:
    a1 = p.load(f)
    b1 = p.load(f)
    c1 = p.load(f)

print(f'Unpickled data: {a1}')
print(f'Unpickled data: {b1}')
print(f'Unpickled data: {c1}')


# list
l1 = ['apple', 23, 56, 78, 'banana', 89-9j, ['a', 'b', 'c']]

# write (pickle)
with open('list1.pkl', 'wb') as f:
    p.dump(l1, f)

# read (unpickle)
with open('list1.pkl', 'rb') as f:
    p_l1 = p.load(f)

print(f'Unpickled list is {p_l1}')


# dictionary
d1 = {
    'name': 'Shridhar',
    'age': 22,
    'course': 'MCA',
    'marks': [85, 90, 88],
    'complex_no': 5 + 7j
}

# write (pickle)
with open('dict1.pkl', 'wb') as f:
    p.dump(d1, f)

# read (unpickle)
with open('dict1.pkl', 'rb') as f:
    p_d1 = p.load(f)

print(f'Unpickled dictionary is {p_d1}')



# custom object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"


p1 = Person('Alpha', 24)

# write object
with open('obj.pkl', 'wb') as f:
    p.dump(p1, f)

# read object
with open('obj.pkl', 'rb') as f:
    p_obj = p.load(f)

print(f'Unpickled object is: {p_obj}')


#multiple objects
l1=[1,2,3,'apple',[2,3,4],89+9j]
d1={1:2,3:4}
s1="Hello Pickling"
with open('all.pkl','wb')as f:
    p.dump(l1, f)
    p.dump(d1, f)
    p.dump(s1, f)
    
with open('all.pkl','rb')as f:
    p_l1=p.load(f)
    p_d1=p.load(f)
    p_s1=p.load(f)
    
print(p_l1)
print(p_d1)
print(p_s1)



#functions
def greet(name):
    return f'Hello {name}'

with open('func.pkl','wb')as f:
    p.dump(greet, f)
    
with open('func.pkl','rb')as f:
    p_f=p.load(f)
    
print(p_f('Alpha'))
print(p_f('Beta'))


    
#data frames
import pandas as pd
data={'Name':['Alpha','Beta'],
      'Age':[12,34],
      'City':['bangalore','Mangalore']}
df=pd.DataFrame(data)
print(df)
print(type(df))

df.to_pickle('df.pkl')
p_df=pd.read_pickle('df.pkl')
print(p_df)
print(type(df))

#Loads and Dumps

