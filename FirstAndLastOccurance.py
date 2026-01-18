def FirstAndLastOccorance(arr,target):
    n=len(arr)
    first=-1
    last=-1
    for i in range(n):
      if arr[i]==target:
         if first==-1:
            first=i
         last=i
    return first,last

arr=[1,1,1,3,4,5,6,7,7,7,7,8,9]
print(FirstAndLastOccorance(arr,target=7))
    
