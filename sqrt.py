import math

def checkPrime(n):
    if n== 1:
        return False

    while True:
        for d in range(2,int(math.sqrt(n))+1):
            if n % d == 0:
                return False
            
        return True


while True:
    n = int(input("give me a number:"))
    if checkPrime(n):
        print (f"That is a prime number {n}")
    else:
        print(f"That is not a prime number {n}")
    
    if n==0 :
        break
