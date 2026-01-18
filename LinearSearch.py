def LinearSearch(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
arr=[4,6,4,8,0,5,0,6,6,-5]
target=4
print(LinearSearch(arr,target))