def Merge(left,right):
    n=len(left)
    m=len(right)
    result=[]
    i,j=0,0
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            left[i]>right[j]
            result.append(right[j])
            j+=1
        
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def MergeSort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=MergeSort(arr[:mid])
    right=MergeSort(arr[mid:])
    return Merge(left,right)
    

print(MergeSort([1,2,6,3,7,2,8,3,9]))