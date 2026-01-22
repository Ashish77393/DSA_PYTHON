def subsequence(index,total,subset,nums,target,result):
    if total==target:
        result.append(subset.copy())
        return
    if total>target or index>=len(nums):
        return
    subset.append(nums[index])
    sum=total+nums[index]
    subsequence(index+1,sum,subset,nums,target,result)
    subset.pop()
    sum=total
    subsequence(index+1,sum,subset,nums,target,result)
index=0
total=0
subset=[]
nums=[1,4,7,3,9,2]
target=9
result=[]
subsequence(index,total,subset,nums,target,result)
print(result)