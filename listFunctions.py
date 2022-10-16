l=list()
l.append(1)
print(l)

l2=l.copy()
print(l2)

while True:
    n=int(input("Give me your age:"))
    print("n:", n)
    if n > 90:
        print(n, ">90")
    elif n > 80:
        print(n, ">80")
    elif n > 70:
        print(n, ">70")
    elif n > 60:
        print (n, ">60")
    elif n < 0:
        print (n,"<0")
        break
    else:
        print(n,"no")
      
