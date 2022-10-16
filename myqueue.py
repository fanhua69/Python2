


class queue:
    __slots__=("my_data", "__c")
   
    def __init__(self, l = None):
        if l!= None:
            self.my_data = l
            self.__c = 123
        
    def push(self, d):
        self.my_data.append(d)
    
    def pop(self):
        if len(self.my_data) == 0:
            return None
        else:        
            return self.my_data.pop(0)
    
    def len(self):
        return len(self.my_data)
    
    def __str__(self):
        s="queue<"
        s+=",".join(map(str,self.my_data))
        s+=">" + str(self.__c)
        return s
    def __eq__(self, o):
        return self.my_data == o.my_data
    
    
class queueDerived(queue):
    __slots__=("d_data","__quantity", "lll")
    #d_data=123
    #__quantity=1234
    def __init__(self, l, d, q):
        super().__init__(l)
        self.d_data= d
        self.__quantity=q
        self.lll="sdfds"
        
    def __str__(self):
        a = super().__str__()
        a+=str(self.d_data)
        a+=str(self.__quantity)
        a+=":" + self.lll
        return a
    
    def __eq__(self,o):
        return super().__eq__(o) and \
               self.d_data == o.d_data and \
               self.lll == o.lll and \
               self.__quantity == o.__quantity
        
        
        
qd = queueDerived([1,2],123,456)
print(qd)
qd2 = queueDerived ([1,2],123,456)
print(qd == qd2)
    