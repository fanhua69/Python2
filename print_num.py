

class IterList:
    def __init__(self, l):
        self.__lst = l
   
   # def __len__(self):
   #     return len(self.__lst)
    
    def __getitem__(self, n):
        if n >= len(self.__lst):
            print("index    fdsfds error")
            raise IndexError
        return self.__lst[n]
    
       
        


il = IterList((1,3,5,6,8,9))

i=iter(il)


try:
    while True:
        n=next(i)
        print(n)
except:
    print("unexpected:")
