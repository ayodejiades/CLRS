from array import *
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
def SelectionSort(array):
    for i in range(0, len(array), 1):
        minIndex = i
        for j in range(i + 1, len(array), 1):
            if (array[j] < array[minIndex]):
                minIndex = j
        if minIndex != i:
            swap(array, i, minIndex)
    return array

arr = array("i", [7, 2, 8, 5])
output = SelectionSort(arr)
print(output)