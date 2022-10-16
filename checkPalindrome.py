

def checkPalindrome(s):
    print(s[::-1])
    if s == s[::]:
        print("is a palindrome")
    else:
        print("is not a palindrome")
        
    i=0
    j=len(s)-1
    
    while(i<=j and s[i]==s[j]):
        i+=1
        j-=1
    print (i, j)
    return i>j

while True:
    s=input ("Give me a string:")
    
    print(s[-3::-1])
    print(checkPalindrome(s))
    if(len(s)==0):
        break


    