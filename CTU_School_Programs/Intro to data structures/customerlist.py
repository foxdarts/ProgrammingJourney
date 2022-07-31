#file for simple customer info input and print

customerlist = list()

customerlist.append(list())
customerlist.append(list())
customerlist.append(list())
customerlist.append(list())
customerlist.append(list())

for i in range(0,5): #can change 5 to be however many customers you have

    customerlist[0].append(input("Customer name: "))
    customerlist[1].append(input("Customer address: "))
    customerlist[2].append(input("City: "))
    customerlist[3].append(input("State: "))
    customerlist[4].append(input("Zip code: "))
    
print(customerlist[4])