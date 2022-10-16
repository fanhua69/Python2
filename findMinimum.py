

def findMinimum(lst):
    if len(lst) == 0:
        return None
    
    n =  lst[0]
    for x in lst:
        if x < n:
            n = x
    
    return n


if __name__ == "__main__":
    l=[-1,1,2,3,4,55,-10]
    print(findMinimum(l))
    