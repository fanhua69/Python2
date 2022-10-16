


def removeDup(l):
    s = set(l[0:3])
    return s

s = input ("Give me a list of numbers:")
s1 = s.split(",")
print(s1)
l = [ int(x) for x in s1]
print(l)
l2 = list(map(int, s1))
print(l2)

l3= removeDup(l2)
print(l3)