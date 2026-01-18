def SearchInsertPostion(arr,target):
    n=len(arr)
    low=0
    high=n-1
    lb=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb
arr=[1,3,5,6,7,9,11,13,17,19]
target=19
print(SearchInsertPostion(arr,target))