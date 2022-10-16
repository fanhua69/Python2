

def createBraces(s):
    rb=[]
    sb=[]
    braces=""
    for b in s:
        if (b == '('):
            sb.append(b)
        elif(b==')'):
            braces='('+braces+')'
            sb=sb[:-1]
            
            if len(sb) == 0:
                rb.append(braces)
                braces=""
            
    return rb


l=createBraces("(()) (  (()))()")
print(l)

            
            
            