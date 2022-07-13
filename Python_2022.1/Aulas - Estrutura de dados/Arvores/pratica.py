class BSTnode:
    def __init__(self, value = None):
        self.data = value
        self.left = self.right = None

    def insert(self, value):
        if not self.data:
            self.data = value
        elif value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.right = BSTnode(value)
        elif value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTnode(value)

    def pre_ordem(self):
        if self.data:
            print(self.data, end='-')
            if self.left:
                self.left.pre_ordem()
            if self.right:
                self.right.pre_ordem()



root = BSTnode()
root.insert(10)
root.insert(20)
root.pre_ordem()