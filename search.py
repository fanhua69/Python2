
def help(data,c,l,r):
    if(l>=r):
        return -1
    
    m = int((l + r)/2)
    print("searching:",m)
    print(data[m],",", c, ",", data[m]==c)
    if(data[m]==c):
        return m
    elif data[m] < c:
        l=m+1
        return help(data,c,l,r)
    else:
        r=m
        return help(data,c,l,r)
        
def search(data,c):
    return help(data,c,0,len(data))

s="012456789"
l=[c for c in s]
print(l)
l.sort()
print(l)

c ='3'

print(search(l,c))