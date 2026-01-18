def FloorCeil(arr,target):
    n=len(arr)
    low=0
    high=n-1
    floor=-1
    ceil=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            floor=arr[mid]
            ceil=arr[mid]
            return floor,ceil
        if arr[mid]>target:
            ceil=arr[mid]
            high=mid-1
        else:
            floor=arr[mid]
            low=mid+1
    return floor,ceil
arr=[1,3,5,7,9,10,12,15,17,20]
target=2
print(FloorCeil(arr,target))