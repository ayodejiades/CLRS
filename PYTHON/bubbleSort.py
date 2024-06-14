from array import *
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
def BubbleSort(array):
    for i in range(0, len(array) - 1, 1):
        for j in range(0, len(array)- i - 1, 1):
            if array[j] > array[j+1]:
                swap(array, j, j + 1)
    return array

arr = array("i", [7, 2, 8, 5])
output = BubbleSort(arr)
print(output)           