def bubblesort(array):
    list = len(array)   #provides a list for number storage
    for n in range(list):  #sets array size
        for l in range(0, list-n-1):  #sets last number per sort
            if array[l] > array[l + 1]:  #swap element function
                array[l], array[l + 1] = array[l + 1], array[l]


list = [3, 44, 45, 10, 15, 16, 9, 11]  #list of numbers to sort

bubblesort(list)

print ("sorted array: ")
for n in range(len(list)):  #prints sorted array
    print ("%d" %list[n])
