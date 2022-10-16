
file=r"/Users/fanhua/exer/python/test2.txt"


try:
    f=open(file,"w")
    try:
        f.write("1 2a 3e\n")
        f.write("2 3b 4f\n")
        f.write("3 4c 5g\n")
        f.write("4 5d 6h\n")
        L = ["asdf","dsf","xcv"]
        f.writelines(L) 
        
    except:
        print("something went wdew wrong when writing")
    finally:
        f.close()
except:
    print("something went wrong")
    

with open(file) as f:
    while True:
        file_eof=f.read(10)
        if file_eof == '':
            print("end of file:")
            ff=f.read(10)
            print("ff:", ff)
            break
        
        print("line:",file_eof)
    
    
