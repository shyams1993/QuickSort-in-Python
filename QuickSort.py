def quickSort(arr,left,right):
    pivot = None
    partitionIndex = None
    if left < right:
        pivot = right
        partitionIndex = partition(arr,pivot,left,right)
        quickSort(arr,left,partitionIndex-1)
        quickSort(arr,partitionIndex+1,right)
    return arr

def partition(arr,pivot,left,right):
    pivotVal = arr[pivot]
    partitionIndex = left
    for i in range(left,right):
        if arr[i] < pivotVal:
            temp = arr[i]
            arr[i] = arr[partitionIndex]
            arr[partitionIndex] = temp
            partitionIndex+=1
    temp = arr[right]
    arr[right] = arr[partitionIndex]
    arr[partitionIndex] = temp
    return partitionIndex

arr = [2,323,2,23,21,67,87,34]
quickSort(arr,0,len(arr)-1)
print(arr)
