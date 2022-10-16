
class A:
    __slots__=["m_data"]
    
    def __init__(self, n):
        self.m_data = n
        
    def __lt__(self, o):
        return self.m_data < o.m_data
    
    def __repr__(self):
        return f'class A, value :{self.m_data}'
    
    def __str__(self):
        return f'{self.m_data}'
    
    def __add__(self,o):
        return A(self.m_data+o.m_data)
    
    def __len__(self):
        return 1
    
    
a= A(3)
b=A(2)

print(a < b)
print(str(a))
print(repr(b))
print(a+b)
print(len(a))
        