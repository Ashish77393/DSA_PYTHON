import time
def BubbleSort(arr):
    n=len(arr)
    curr=time.localtime
    print(curr)
    for i  in range(n):
        is_swap=False
        for j in range(n):
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                is_swap=True
        if is_swap==False:
            break
                
    return arr
arr=[2,5,2,4,1,4,2,4,22,22]
print(BubbleSort(arr))