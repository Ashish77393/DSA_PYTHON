def arraySorted(arr):
    n=len(arr)
    if n==1:
        return True
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
arr=[1,2,4,5,6,7,8]
print(arraySorted(arr))