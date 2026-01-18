def Rearrange(arr):
    list=[]
    n=len(arr)
    for i in range(n):
        if arr[i]>0 and i%2!=0:
            list.insert(i,arr[i])
        list.insert(i,arr[i])
    return list
arr=[5,10,-1,-1,-10,6]
print(Rearrange(arr))