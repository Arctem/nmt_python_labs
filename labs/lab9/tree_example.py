class Tree:
    def __init__(self, item, left=None, right=None):
        self.left = left
        self.right = right
        self.item = item

    def __iter__(self):
        if self.left:
            for i in self.left:
                yield i

        yield self.item

        if self.right:
            for i in self.right:
                yield i

        raise StopIteration

a = Tree(1, Tree(2), Tree(3))
print(a)
for i in a:
    print(i)

for i in a:
    print(i)