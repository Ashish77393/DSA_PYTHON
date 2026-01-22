def printSubsequence(idx, nums, sublist):
    if idx >= len(nums):
        print(sublist)
        return
    sublist.append(nums[idx])
    printSubsequence(idx + 1, nums, sublist)
    sublist.pop()
    printSubsequence(idx + 1, nums, sublist)


nums = [1, 2, 3]
printSubsequence(0, nums, [])
