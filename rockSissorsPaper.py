
import random as rd
from enum import Enum

class Result(Enum):
    LOSE = 0
    BALANCED = 1
    WIN =2

def checkRockScissorsPaper(l):
    if len(l) != 2:
        return Result.BALANCED
    elif l[0]==l[1]:
        return Result.BALANCED
    else:
        d={str([0,1]):True, str([1,2]):True, str([2,0]): True}
        if str(l) in d.keys():
            return Result.WIN
        else:
            return Result.LOSE


while True:
    print("0 -- Rock, 1-- Scissors, 2-- Paper")
    n = int (input("your choice :"))
    
    
    di ={ 0 : "Rock", 1:"Scissors", 2: "Paper"}
    
#    m = rd.randint(0,2)
#    print(f"Computer chose: {di[m]}")
    
    m = rd.choice([0,1,2])
    print("Computer chose {}".format(di[m]))

    l=[n,m]
    print("str(l):",str(l))
    r = checkRockScissorsPaper(l)
    o=print(r)
    
    
    