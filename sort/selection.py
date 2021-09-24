from util import isSorted, testArray
import time

###########

def selectionSort(arr):
    for i in range(0, len(arr)):
        minIndex = i
        for j in range(i, len(arr)):
            # get minimum index of sub array
            if(arr[j] < arr[minIndex]):
                minIndex = j
        if(minIndex != i):
            # swap
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    
    return arr



###########
startTime = time.time()
result = selectionSort(testArray)
endTime = time.time()

print("Initial Array:")
print(testArray)
print("Result Array:")
print(result)
print("Sorted: " + str(isSorted(result)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
