

def rightRotateList(lst, k):
    if len(lst) == 0:
        k = 0
        
    else:
        k = k%len(lst)
    
    return lst[-k:]+lst[:-k]
    
if __name__ == '__main__':
    l = [1,2,3,4,5]
    print(l[-2:])
    print(l[:-2])
    
    
    print(rightRotateList(l,2))
    