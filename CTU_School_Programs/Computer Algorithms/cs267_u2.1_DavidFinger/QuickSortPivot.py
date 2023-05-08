import timeit
import random



def quicksort(array):
    quicksort2(array, 0, len(array) - 1)

def quicksort2(array, low, hi):
    if low < hi:
        p = partition(array,low, hi)
        quicksort2(array, low, p - 1)
        quicksort2(array, p + 1, hi)

def getpivot(array, low, hi):
    mid = (hi + low)  // 2
    pivot = hi
    if array[low] < array[mid]:
        if array[mid] < array[hi]:
            pivot = mid
    elif array[low] < array[hi]:
        pivot = low
    return pivot

def partition(array, low, hi):
    pivotindex = getpivot(array, low, hi)
    pivotvalue = array[pivotindex]
    array[pivotindex], array[low] = array[low], array[pivotindex]
    border = low

    for i in range(low, hi + 1):
        if array[i] < pivotvalue:
            border += 1
            array[i], array[border] = array[border], array[i]
    array[low], array[border] = array[border], array[low]

    return (border)




list = [random.randint(1, 100) for i in range(1000)]  #list of numbers to sort



quicksort(list)

print ("Quick Sorted array: ")
print (list, end = ",")
