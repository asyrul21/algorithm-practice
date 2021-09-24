from util import isSorted, testArray
import time

###########

def partition(arr, start, end):
    pivot = arr[end]
    indexOfValueLessThanPivot = start - 1

    for j in range(start, end):
        if(arr[j] < pivot):
            indexOfValueLessThanPivot+= 1
            # swap
            arr[j], arr[indexOfValueLessThanPivot] = arr[indexOfValueLessThanPivot], arr[j]
    
    # swap last item, since we started i at -1
    arr[indexOfValueLessThanPivot + 1], arr[end] = arr[end], arr[indexOfValueLessThanPivot + 1]
    return indexOfValueLessThanPivot + 1


def quickSort(arr, start, end):
    if(start < end):
        # get partition array on pivot
        # sort left side and right side of pivot
        # returns the partitionIndex:
        # the index with the value at correct position
        pi = partition(arr, start, end)

        # recursive call
        quickSort(arr, 0, pi - 1)
        quickSort(arr, pi + 1, end)

    
    return arr



###########
startTime = time.time()
result = quickSort(testArray, 0, len(testArray) - 1)
endTime = time.time()

print("Initial Array:")
print(testArray)
print("Result Array:")
print(result)
print("Sorted: " + str(isSorted(result)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
