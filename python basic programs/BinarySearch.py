#this is for a binary search.  binary search is a divide and concour algorithm that allows a search of a list without checking each element of the searched list.  

import random


def binary_search(section, WValue, lowvalue = None, HighValue = None):
    
    if lowvalue is None:
        
        lowvalue = 0 #if there isnt a lowvalue set the low to 0
        
    if HighValue is None:
        
        highvalue = len(section) - 1 #highest value is the total number of numbers in the search -1 as index starts at 0
        
    if highvalue < lowvalue:
        
        return -1 #if the number isnt in the list immediatly return that 
    
    MidPivot = (lowvalue + highvalue) // 2 #midpoint is the lowest value in the search section + the highest value in the search section of the (list, array, dictionary) that we feed into the section that we are searching divided by 2 (//2)
    
    if section[MidPivot] == WValue:
        
        return MidPivot #states simply that if the midpoint of the section is our number we are looking for, return that number
    
    elif WValue < section[MidPivot]:
        
        return binary_search(section, WValue, lowvalue, MidPivot - 1) #else if the wanted value(WValue) isless than the midpivot piint run a search of everything lower than the midpoint
    
    else: 
        
        return binary_search(section, WValue, HighValue, MidPivot + 1) #run a search for everything higher than the midpoint
        
        
        
        
if __name__ == '__main__':
    
    section = [] #fill whatever list values you want to search through here
    
    WValue = "" #replace "" with value you are looking for
    
    print(binary_search(section, WValue)) #prints the search area and the value you are looking for)


#-------------------------------------------------------------------------------

#this is aversion of binary search from school projects with sorting functions built in



# def quicksort(array):
    
#     quicksort2(array, 0, len(array) - 1)

# def quicksort2(array, low, hi):
    
#     if low < hi:
    
#         p = partition(array,low, hi)
    
#         quicksort2(array, low, p - 1)
    
#         quicksort2(array, p + 1, hi)

# def getpivot(array, low, hi):
    
#     mid = (hi + low)  // 2
    
#     pivot = hi
    
#     if array[low] < array[mid]:
    
#         if array[mid] < array[hi]:
    
#             pivot = mid
    
#     elif array[low] < array[hi]:
    
#         pivot = low
    
#     return pivot

# def partition(array, low, hi):
    
#     pivotindex = getpivot(array, low, hi)
    
#     pivotvalue = array[pivotindex]
    
#     array[pivotindex], array[low] = array[low], array[pivotindex]
    
#     border = low

#     for i in range(low, hi + 1):
    
#         if array[i] < pivotvalue:
    
#             border += 1
    
#             array[i], array[border] = array[border], array[i]
    
#     array[low], array[border] = array[border], array[low]

#     return (border)




# list = [random.randint(1, 10) for i in range(1000)]  #list of numbers to sort



# quicksort(list)

# print ("Quick Sorted array: ")

# print (list, end = ",")

# searchvalue = [random.randint(1,10) for i in range (1)]



# print('\n'f"Search value is: {searchvalue}")

# def binary_search(list, searchvalue):
	
#     LowValue = 1
	
#     HighValue = len(list)-1
	
#     found = "Not Found"
	
#     while(  LowValue <= HighValue and not found):
		
#         mid =  LowValue + HighValue // 2
		
#         if list[mid] == searchvalue :
			
#             found = True
		
#         elif searchvalue < list[mid]:
			
#             HighValue = mid - 1
			
#         else:
			
#             LowValue = mid + 1
	
    
#         return "element found"



# print(binary_search([list], searchvalue))