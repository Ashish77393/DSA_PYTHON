def listCount(n,m):
    hash_list=[0]*11
    for num in n:
        hash_list[num]+=1
    for num in m:
        if num<1 or num>10:
            print("Not Found")
        else:
            print(num ,":",hash_list[num])
n=[2,3,5,2,4,6,5,7,4,7,4]
m=[22,4,3]
listCount(n,m)
