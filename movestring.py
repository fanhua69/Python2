
def moveString(strings,startstring):

    i = 0
    for j in range(len(strings)):
        if strings[j].startswith(startstring):
            s=strings[j]
            for k in range(j,i,-1):
                strings[k]=strings[k-1]
            strings[i]=s
            i=i+1
    
    return strings
            
                
    

l=["abc","starta","def","ghi","startb", "sdfsdaf s", "startc", "startd"]
l2=moveString(l,"start")
print(l2)