def printSubarray(list):
    n=len(list)
    for i in range(n):
        mylist=[]
        for j in range(i,n):
            mylist.append(list[j])
            print( mylist)
list=[1,2,3]
printSubarray(list)