
import random as rd

s=[]
s.append("0123456789")
s.append("abcdedghijklmnopqrstuvwxyz")
s.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
s.append("~!@#$%^&()_+=-<>[]{}|")

passwordLen = 341

password=""
for i in range(passwordLen):
    password+=rd.choice(rd.choice(s))
    
print(password)
    



