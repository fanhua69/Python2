import csv

def csv_reader(filename):
    for row in open(filename,"r"):
        yield row
        
for s in csv_reader("1.csv"):
    print (s)
        
    
