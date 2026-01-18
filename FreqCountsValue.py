def FreqCountsValue(arr):
    freq_map={}
    n=len(arr)

    # 1st  method
    # for i in range(n):
    #     if arr[i] in freq_map:
    #         freq_map[arr[i]]+=1
    #     else:
    #         freq_map[arr[i]]=1
    # return freq_map[2]


    # 2nd method
    for i in range(n):
        freq_map[arr[i]]=freq_map.get(arr[i],0)+1
    return freq_map
arr=[2,3,4,2,4,2,4,2,5,2]
print(FreqCountsValue(arr))