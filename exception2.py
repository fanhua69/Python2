import sys

'''
except OSError as err:
    print(err)
    print ("OS error: {0}".format(err))
'''

try:
    f=open("test.txt")
    s=f.readline()
    n=int(s)
#except ValueError:
#    print (" Counld not convert data to an integer.")
#except BaseException as err:
#    print(err)
#    print (type(err))
#    print(f"Unexpected error happened:  {err=}, ewqrewr {type(err)=}")
except BaseException as err:
    print("dsfd", err, type(err))
else:
    print("unexpected   fdsaf sd ")
finally:
    print("This is always exicuted")
    

