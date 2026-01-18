def ReverseArray(arr):
    n=len(arr)
    if n==0:
        return 
    print(arr[n-1])
    ReverseArray(arr[:-1])   
    
arr=[2,5,3,5,2,5,3]
print(ReverseArray(arr))