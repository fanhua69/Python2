

def rearrange(lst):
    
    leftMostPosEle = 0
    
    for cur in range(len(lst)):
        if lst[cur] < 0:
            if cur != leftMostPosEle:
                lst[cur], lst[leftMostPosEle] = lst[leftMostPosEle], lst[cur]
                
            
            leftMostPosEle+=1
            print(lst, leftMostPosEle)
            
    
if __name__ == "__main__":
    lst = [2,3,-1,-3, -9,-10,-11,-12,1]
    
    rearrange(lst)
    print(lst)
        
    