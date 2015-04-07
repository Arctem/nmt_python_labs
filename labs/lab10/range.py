class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = None
        return self

    def __next__(self):
        if self.current is None:
            self.current = self.start
        else:
            self.current += 1

        if self.current >= self.end:
            raise StopIteration
        else:
            return self.current

r = MyRange(1, 10)
for i in r:
    print(i) #prints 1, 2, 3, ..., 9
