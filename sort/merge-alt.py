from util import isSorted, testArray
import time

# this approach preserves the index number or result array throughout recusion

###########

def merge(arr, tempArray, startIdx, midIdx, endIdx):
    i = startIdx
    j = midIdx + 1
    k = startIdx

    while i <= midIdx and j <= endIdx:
        if(arr[i] <= arr[j]):
            tempArray[k] = arr[i] # tempArray will take the value of UPDATED original array
            i += 1
        else:
            tempArray[k] = arr[j]
            j += 1
        k+= 1

    while i <= midIdx:
        tempArray[k] = arr[i]
        i += 1
        k += 1

    while j <= endIdx:
        tempArray[k] = arr[j]
        j += 1
        k += 1

    # update the orginal array
    for loop_var in range(startIdx, endIdx + 1):
        arr[loop_var] = tempArray[loop_var]



def _mergeSort(arr, tempArray, startIndex, endIndex):
    if(startIndex < endIndex):
        print(startIndex)
        mid = (endIndex + startIndex) // 2

        _mergeSort(arr, tempArray, startIndex, mid)
        _mergeSort(arr, tempArray, mid+ 1, endIndex)

        merge(arr, tempArray, startIndex, mid, endIndex)

       
        # print(tempArray)
        # return tempArray



def mergeSort(arr):
    # create temp array
    tempArr = [0]*len(arr)

    _mergeSort(arr,tempArr, 0, len(arr)- 1) 

    print(arr)
    print(tempArr)
    
    return tempArr



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
