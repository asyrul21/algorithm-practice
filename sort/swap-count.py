from util import isSorted, testArray3, testArray2, testArray4
import time

###########

def minSwap(arr):
    swaps = 0
    tempArray = arr.copy()
    tempArray.sort()
    h = {}

    print(arr)

    # build dictionaries of index
    for i in range(len(arr)):
        h[arr[i]] = i

    initialValue = 0
    for i in range(0, len(arr)):
        if(arr[i] != tempArray[i]):
            swaps += 1
            # store initial value
            initialValue = arr[i]

            # swap with correct value
            correctIndexForValue = h[tempArray[i]]
            arr[i], arr[correctIndexForValue] = arr[correctIndexForValue], arr[i]

            # update dictionary
            h[initialValue] = correctIndexForValue
            h[correctIndexForValue] = i

    return swaps


###########
workingArray = testArray2
startTime = time.time()
swapCounts = minSwap(workingArray)
endTime = time.time()

print("Minimum swap count:")
print(swapCounts)
print("Sorted: " + str(isSorted(workingArray)))
print("Execution time:")
print(str(endTime - startTime)+ " ms")
