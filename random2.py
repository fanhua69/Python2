import random

def checkIndex(l,threshold):
    lr = []
    for i in range(len(l)):
        if l[i] < threshold:
            lr .append(i)
            
    return lr


x = [1,2,3]
y=[4,5,6]
all = [a *b for a in x  for b in y]
print (all)
            
            
a= random.sample(range(100),10)
b=random.sample([1,2,3],2)
print(b)