

    
def retate_chr(c):
    rot_by = 3
    c=c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    else:
        return chr(rotated_pos-26)
    
    
print(list(map(retate_chr,"yza")))

def isPos(k):
    return k >= 0


print(list(filter(isPos,[-1,1,2,3])))

    
    
    
    
import functools
import operator
import os
import os.path

files=os.listdir(os.path.expanduser("~"))
print(files)
print(type(files))
del files[0]

for x in files:
    print(x)
    

l=[1,2,3,4]
n=functools.reduce(operator.add,l)
print(type(n))

print(sum(l))
             


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    