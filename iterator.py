l=[1,2,3,4,5]
l_iter=iter(l)
print(l_iter)

print(next(l_iter))

print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
print(l_iter.__next__())
# print(l_iter.__next__())
# print(l_iter.__next__())

l_iter=iter(l)
print(next(l_iter))


str="Python Programming"
s_iter=iter(str)
print(type(str), type(s_iter))

print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))


t=(1,2,3,4,5)
t_iter=iter(t)
print(type(t), type(t_iter))

d={1:2,3:4,5:6}
d_iter=iter(d)
print(type(d), type(d_iter))







