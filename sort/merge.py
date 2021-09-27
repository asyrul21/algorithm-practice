from util import isSorted, testArray
import time

###########
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
