

def find_first_unique(lst):
    s=set()
    print(type(s))
    for x in lst:
        if x in s.keys():
            s[x]+=1
        else:
            s[x]=1
    
    for x in lst:
        if s[x] == 1:
            return x
        
        
if __name__ == "__main__":
    l=[1,2,3,4,5,6,1,2,3,4,5]
    print(find_first_unique(l))