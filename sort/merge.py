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


def mergeSort(arr):
    
    # only do if there are more than 1 elements
    if(len(arr) > 1):
        # get the middle index
        mid = (len(arr) // 2)

        # divide to left
        leftSide = arr[:mid]

        # divide to right
        rightSide = arr[mid:]

        # recursive call to both left and right
        mergeSort(leftSide)
        mergeSort(rightSide)

        # the merging
        i = j = k = 0

        # compare and select the lesser value
        while i < len(leftSide) and j < len(rightSide):
            if(leftSide[i] < rightSide[j]):
                arr[k] = leftSide[i]
                i += 1
            else:
                arr[k] = rightSide[j]
                j+= 1
            k+= 1

        # check for remaining values
        while i < len(leftSide):
            arr[k] = leftSide[i]
            i+= 1
            k+= 1

        while j < len(rightSide):
            arr[k] = rightSide[j]
            j += 1
            k += 1
    
    return arr



###########
startTime = time.time()
result = mergeSort(testArray)
endTime = time.time()

print("Initial Array:")
print(testArray)
print("Result Array:")
print(result)
print("Sorted: " + str(isSorted(result)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
