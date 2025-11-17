l=[1,2,3,4]
s='hello'
t=(1,2,3)
s={1,2,3}
d={1:2,3:4}
n=123

print(dir(l))

print(l.__class__)
print(l.__sizeof__())
print(l.__add__([5]))
print(l.__contains__(5))
print(l.__hash__)
print(l.__contains__(1))
print(l.__iter__())


print(dir(s))
print(s.__class__)
# print(s.__add__('world'))
print(s.__contains__('h'))  

print(dir(t))
print(t.__class__)
print(t.__add__((4,5)))
print(t.__contains__(2))

print(dir(s))
print(s.__class__)
# print(s.__add__(' world'))
print(s.__contains__('e'))

print(dir(d))
print(d.__class__)
print(d.__contains__(1))
print(d.__getitem__(3))

print(dir(n))
print(n.__class__)
print(n.__add__(10))
print(n.denominator)
n1=34+9j
print(n1.imag)
print(n1.real)
print(n.numerator)
print(n.bit_length())
print(n.bit_count())




