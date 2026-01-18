# def BinarySearch(arr,target):
#     n=len(arr)
#     low=0
#     high=n-1
#     while(low<=high):
#         mid=(low+high)//2
#         if arr[mid]==target:
#             return mid
#         elif arr[mid]<target:
#             low=mid+1
#         elif arr[mid]>target:
#             high=mid-1
#     return "does not exits"
def BinarySearch(arr,low,high,target):
    if low>high:
        return -1
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        return BinarySearch(arr,mid+1,high,target)
    else:
        return BinarySearch(arr,low,mid-1,target)
arr=[1,2,3,4,5,6,7,8,9]
target=7
low=0
high=len(arr)-1
print(BinarySearch(arr,low,high,target))