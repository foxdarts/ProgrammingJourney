




class Node(object):
    def __init__(self, d, n = None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.get_data

    def set_data(self, d):
        self.set_data = d

class linkedlist(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size(self):
        return self.size

    def __add__(self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1

    def __remove__(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -=1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False

    def find(self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            elif this_node.get_next() == None:
                return False
            else:
                this_node = this_node.get_next()

def main():
    list = linkedlist()
    list.__add__(9)
    list.__add__(13)
    list.__add__(2)
    
    print(list)


if __name__ == '__main__':
    main()
