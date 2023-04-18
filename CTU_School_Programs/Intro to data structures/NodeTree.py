class Node(object):   #creates node class

    def __init__(self, data):

        self.left = None  #adds left side of tree
        self.right = None  #adds right side of tree
        self.data = data  #creates data within node

    def insert(self, data):
        if self.data:
            if data < self.data:  #adds lower values to left side tree
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:  #adds higher values to left side tree
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):  #prints full tree
        #if self.left:
            #self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

root = Node(3)
root.insert(2)
root.insert(4)
root.insert(6)
root.insert(5)
root.insert(10)

root.PrintTree()  #prints values based on which side of tree they fall on
