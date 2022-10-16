def findSecondBig(lst):
    
    max = float('-inf')
    secondmax=float('-inf')
    
    for x in lst:
        if x > max:
            secondmax = max
            max = x
        elif x > secondmax:
            secondmax = x
    
    return secondmax
            
        