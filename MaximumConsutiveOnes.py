def MaximumConsutiveOnes(arr):
    n=len(arr)
    count=0
    maximum=0
    for i in range(n):
        if arr[i]==1:
            count+=1
            maximum=max(maximum,count)
        else:
            count=0
    return maximum


arr=[0,1,1,1,0,1,1,1,1,0]
print(MaximumConsutiveOnes(arr))