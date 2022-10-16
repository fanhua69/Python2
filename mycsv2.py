

def fr(filename):
    with open(filename,"r") as f:
        for r in f:
            yield r
            
            
for  x in fr("1.csv"):
    print(x)    