def Subsequence(index,total,subset,nums,target,result):
    if total==target:
        result.append(subset.copy())
        return 1
    if index>=len(nums) or total>target:
        return 0
    subset.append(nums[index])
    sum=total+nums[index]
    c1=Subsequence(index+1,sum,subset,nums,target,result)
    subset.pop()
    sum=total
    c2=Subsequence(index+1,sum,subset,nums,target,result)
    return c1+c2

index=0
total=0
subset=[]
nums=[5,9,4]
target=9
result=[]
count=0
s=Subsequence(index,total,subset,nums,target,result)
print(s)

    
