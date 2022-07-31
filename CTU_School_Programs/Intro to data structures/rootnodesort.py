#file for a root node sort with side printing

class Node:
    def __init__(self):
        self.right = None
        self.left = None
        self.data = list()

def addguest(root, guest):
    if guest < root.data[0]:
         if root.right == None:
             root.right = Node()
             root.right.data.append(guest)
         else:
             addguest(root.right, guest)
    else:
        if guest > root.data[0]:
            if root.left == None:
                root.left = Node()
                root.left.data.append(guest)
            else:
                addguest(root.left, guest)
        else:
            root.data.append(guest)

def printguests(root):
    if root == None:
        return
    print(root.data)
    printguests(root.right)
    printguests(root.left)


if __name__ == '__main__':
    root = Node()
    root.data.append("l") #set split letter here
    for i in range(0,5):
        addguest(root, input("guest name: "))
    print("on the right: ")
    printguests(root.right)
    print("on the left: ")
    printguests(root.left)
