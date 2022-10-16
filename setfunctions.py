

s1=set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)

s2={2,3,4,5,6}
s3={11,14,12,14,15,16}

s4={2,3,4}

d={}
print(type(s2))
print(type(d))

s=s1.difference(s2)
print("difference:", s)

s=s1.union(s2)
print("union:",s)

#s=s1.difference_update(s2)
#print("difference_update:",s1)

s=s1.intersection(s3)
print("intersection:",s, s1,s2)

b=s1.isdisjoint(s3)
print("is disjoint:", s1,s3,b)

b=s4.issubset(s1)
print("issubset:", s4, s1, b)


b=s1.issuperset(s4)
print("issuperset:", s1,s4,b)

z = s1.symmetric_difference(s2)
print("symmetric_differene:",z)
z= s1.symmetric_difference_update(s2)
print("s1", s1)

if(len(s1) > 0):
    s1.pop()
    print("after pop:",s1)

s1.clear()
print("after clear:",s1)




