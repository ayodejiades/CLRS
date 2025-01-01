from array import *  # noqa: F403
def InsertionSort(array):
    for i in range(1, len(array), 1):
        key = array[i]
        j = i - 1
        while(j >=0 and array[j] > key):
            array[j+1] = array[j]
            j-=1
        array[j+1]=key
    return array

arr = array("i", [7, 2, 8, 5])  # noqa: F405
output = InsertionSort(arr)
print(output)   