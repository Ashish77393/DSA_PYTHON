def RotateArrayK(arr,k):
    n=len(arr)
    k=n-k
    # if n<=1:
    #     return arr
    # for _ in range(k-1):
    #     temp=arr[-1]
    #     for j in range(n-1,0,-1):
    #       arr[j]=arr[j-1]
    #     arr[0]=temp
    # return arr


    #second method 
    # for _ in range(k):
    #     e=arr.pop()
    #     arr.insert(0,e)

    #Third method
    arr[:]=arr[n-k:]+arr[:n-k]



    return arr
arr=[1,2,3,4,5,6,7]
k=3
print(RotateArrayK(arr,k))