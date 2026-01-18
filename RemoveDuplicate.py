def RemoveDuplicate(arr):
    # n=len(arr)
    # count=0
    # i=0
    # while i < len(arr):
    #     j = i + 1
    #     while j < len(arr):
    #         if arr[i] == arr[j]:
    #             arr.pop(j)

    #                 # remove duplicate
    #                  # count duplicate
    #         else:
    #             j += 1
    #     count+=1       
    #     i += 1
    # return count,arr




    # dict_maps={}
    # for i in range(len(arr)):
    #     dict_maps[arr[i]]=0
    # j=0
    # for k in dict_maps:
    #     arr[j]=k
    #     j+=1
    # return j

    

     n=len(arr)
     i=0
     j=i+1
     if n==1:
          return 1
     while j<n:
          if arr[i]!=arr[j]:
               i+=1
               arr[i],arr[j]= arr[j],arr[i]
          j+=1
     return i+1
               
arr=[1,2,3,3,3,4,4,5,5,6,7,8,9,9]
print(RemoveDuplicate(arr))
