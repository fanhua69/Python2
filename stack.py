

class Stack:
    __slots__=["m_data"]
    
    def __init__(self, l=None):
        if l!=None:
            self.m_data = l
        else:
            self.m_data=list()
        
    
    def push(self,data):
        self.m_data.append(data)
        pass
    
    def pop(self):
        if(len(self.m_data) == 0):
            return None
        else:
            return self.m_data.pop(-1)
    
    def len(self):
        return len(self.m_data)
    
    def __str__(self):
        return "@"+",".join(map(str,self.m_data))+"@"
       
        
s=Stack([1,2,3])
print(s)
s.push(4)
print(s)
print(s.pop())
print(s)

s2=Stack()
print(s2)
