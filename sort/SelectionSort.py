def SelectionSort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[min_index]<arr[j]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr
arr=[2,45,2,5,3,56]
print(SelectionSort(arr))