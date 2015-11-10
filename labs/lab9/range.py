class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        current = self.start
        while current < self.end:
            yield current
            current += 1
        raise StopIteration

r = MyRange(1, 10)
for i in r:
    print(i) #prints 1, 2, 3, ..., 9