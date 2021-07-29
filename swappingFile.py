
def swapFileData():
    f1 = input("Enter the file name.")
    f2 = input("Enter the second file name.")
    
    with open(f1,'r')as a:
        data1 = a.read()

    with open(f2,'r')as b:
        data2 = b.read()
    
    with open(f1,'w')as a:
        a.write(data2)

    with open(f2,'w')as b:
        b.write(data1)

swapFileData()