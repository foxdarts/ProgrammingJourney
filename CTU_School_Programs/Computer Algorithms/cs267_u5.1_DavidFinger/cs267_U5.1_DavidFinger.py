int_max = 999999999


def optimalSearchtree(keys, freq, n):

    cost = [[0 for x in range(n)]
               for y in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for l in range(2,n +1):
        for i in range(n - l +2):
            j = i + l - 1
            if i >= n or j >= n:
                break
            cost[i][j] = int_max

            for r in range(i, j + 1):
                c = 0
                if (r > i):
                    c += cost[i][r - 1]
                if (r < j):
                    c += cost[r + 1][j]
                c += sum(freq, i, j)
                if (c < cost[i][j]):
                    cost[i][j] = c
    return cost[0][n - 1]

def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)



    def Printtree(self):
        if self.left:
            self.left.Printtree()
        print(self.data),
        if self.right:
            self.right.Printtree()

root = Node(8)
root.insert(4)
root.insert(2)
root.insert(1)
root.insert(3)
root.insert(6)
root.insert(5)
root.insert(7)
root.insert(12)
root.insert(10)
root.insert(9)
root.insert(11)
root.insert(14)
root.insert(13)
root.insert(15)

root.Printtree()