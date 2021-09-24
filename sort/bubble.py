from util import isSorted, testArray
import time

###########

def bubbleSort(arr):
    while(True):
        if(isSorted(arr)):
            break
        else:
            for i in range(0, len(arr)):
                for j in range(i, len(arr)):
                    if arr[j] < arr[i]:
                        # swap
                        arr[j], arr[i] = arr[i], arr[j]
    return arr


###########
startTime = time.time()
result = bubbleSort(testArray)
endTime = time.time()

print("Initial Array:")
print(testArray)
print("Result Array:")
print(result)
print("Sorted: " + str(isSorted(result)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
