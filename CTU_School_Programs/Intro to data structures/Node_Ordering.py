
class Node(object):

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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self, root):
        IOT = []
        if root:
            IOT = self.inorderTraversal(root.left)
            IOT.append(root.data)
            IOT = IOT + self.inorderTraversal(root.right)
        return IOT

    def PreorderTraversal(self, root):
        POT = []
        if root:
            POT.append(root.data)
            POT = POT + self.PreorderTraversal(root.left)
            POT = POT + self.PreorderTraversal(root.right)
        return POT

    def PostorderTraversal(self, root):
        PST = []
        if root:
            PST = self.PostorderTraversal(root.left)
            PST = PST + self.PostorderTraversal(root.right)
            PST.append(root.data)
        return PST


root = Node(100)
root.insert(60)
root.insert(50)
root.insert(67)
root.insert(110)
root.insert(109)
root.insert(111)
print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))
