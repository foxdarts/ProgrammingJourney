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




list = [random.randint(1, 10) for i in range(1000)]  #list of numbers to sort



quicksort(list)

print ("Quick Sorted array: ")
print (list, end = ",")
searchvalue = [random.randint(1,10) for i in range (1)]



print('\n'f"Search value is: {searchvalue}")

def binary_search(list, searchvalue):
	
    first = 1
	
    last = len(list)-1
	
    found = "Not Found"
	
    while( first <=last and not found):
		
        mid = (first + last)//2
		
        if list[mid] == searchvalue :
			
            found = True
		
        elif searchvalue < list[mid]:
			
            last = mid - 1
			
        else:
			
            first = mid + 1
	
    
        return "element found"


if __name__ == '__main__':

    print(binary_search([list], searchvalue))



