def LongestConsutive(arr):
    # maximum=float('-inf')
    # n=len(arr)
    # for i in range(n):
    #     first=arr[i]
    #     count=1
    #     while first+1 in arr:
    #             count+=1
    #             first+=1
    #     maximum=max(maximum,count)
    # return maximum
    smaller=float('-inf')
    count=0
    longest=0
    arr.sort()
    n=len(arr)
    for i in range(n):
        nums=arr[i]
        if nums-1==smaller:
            count+=1
            smaller=nums
        elif nums-1!=smaller:
            count=1
            smaller=nums
        longest=max(longest,count)
    return longest
arr=[1,99,101,98,2,5,4,3,100]
print(LongestConsutive(arr))
