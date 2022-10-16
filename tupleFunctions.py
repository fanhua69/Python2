

t= tuple((22,45,23,22, 78,"david", 6.89, "david"))
print(type(t))
print(len(t))
print("count of 'david'",t.count("david"))
print("index of 22 :", t.index(22))

t2=sorted((1,2,3,6,98,5,4))
print("after sorted:", t2)

t2=(1,2,3,6,98,5,4)
print("min of tuple:", min(t2))
print("max of tuple:", max(t2))
print("sum of tuple:", sum(t2))

l1=[1,2,3,34,-1]
print("min list:", min(l1))
print("max list:", max(l1))
print("sum list:", sum(l1))

s1={1,2,3,67,4,3,1,2}
print(type(s1))
print("min in set:", min(s1))
print("max in set:", max(s1))
print("sum in set:", sum(s1))

d2={1:11, 2:22, 3:33}
print("sum of dict:",sum(d2))
print("min of dict:",min(d2))
print("max of dict:",max(d2))
print(type(d2.values()))
print("sum of values of dict:",sum(d2.values()))

#print(help(d2))

r = d2.setdefault(4,44)
print(r)
r = d2.setdefault(4,45)
print(r)





