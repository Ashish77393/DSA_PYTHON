def Largest(arr):
    largest=arr[0]
    n=len(arr)
    for i in range(1,n):
        largest=max(largest,arr[i])
    return largest
arr=[-1,-4544,-33,-2,-436,-88,-4,-9,-5,-433,0]
max=Largest(arr)
print("largest number is " ,max)