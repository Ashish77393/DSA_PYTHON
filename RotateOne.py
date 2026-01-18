def RotateOne(arr):
    n=len(arr)
    arr[:]=[arr[n-1]]+arr[0:n-1]
    return arr
arr=[1,2,3,4,5,6,8,9]
print(RotateOne(arr))