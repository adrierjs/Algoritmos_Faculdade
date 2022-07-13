class BSTnode:
    def __init__(self, value = None):
        self.data = value
        self.left = self.right = None


    def insert(self, value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if not self.left:
                self.left = BSTnode(value)
            else:
                if self.left:
                    self.left.insert(value)
        elif value > self.data:
            if not self.right:
                self.right = BSTnode(value)
            else:
                if self.right:
                    self.right.insert(value)

    def pai_filho(self):
        if self.data:
            if self.left:
                if self.left.left or self.left.right:
                    print(self.left.data)
                self.left.pai_filho()
            if self.right:
                if self.right.left or self.right.right:
                    print(self.right.data)
                self.left.pai_filho()


root = BSTnode()
root.insert(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(20)
root.insert(25)
root.insert(13)
root.insert(2)
root.pai_filho()







