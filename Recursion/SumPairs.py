def SumPairs(idx,target,nums,total,result,subset):
    if total==target:
        result.append(subset.copy())
        return
    if total>target or idx>=len(nums):
        return 
    sum=total+nums[idx]
    subset.append(nums[idx])
    SumPairs(idx,target,nums,sum,result,subset)
    sum=total
    subset.pop()
    SumPairs(idx+1,target,nums,sum,result,subset)
nums=[2,3,6,7]
target=8
result=[]
subset=[]
SumPairs(0,target,nums,0,result,subset)
print(result)



     

