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
    