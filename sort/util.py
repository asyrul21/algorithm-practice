testArray = [2 ,3,14, 5, 16, 19, 21, 44, 7, 90, 55, 42]

def isSorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(0, len(arr) - 1))