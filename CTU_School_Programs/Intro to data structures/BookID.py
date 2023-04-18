bookID = []

bookID.append('1000')  #append used as push
bookID.append('2000')
bookID.append('3000')
bookID.append('4000')

print(bookID)

bookID.pop()  #poping element 4000 from stack
bookID.pop()  #poping element 3000 from stack

print(bookID)  #shows elements leaving from the top of the stack

bookID.pop()  #poping element 2000 from stack
bookID.pop()  #poping element 1000 from stack

print(bookID)  #shows empty stack.
