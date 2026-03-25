m,n=int(input()),int(input())
l=list(range(m,n+1))
c=0
for i in l:
    x=i*i
    c+=x
print(c)



print(sum(i*i for i in range(int(input()), int(input())+1)))



from functools import reduce
m,n=int(input()),int(input())+1
x=map(lambda i: i*i, range(m,n))