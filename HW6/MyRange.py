class MyRange:
    def __init__(self, start, end, step=1):
        self.__start = start
        self.__end = end
        self.__step = step

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start):
        self.__start = start

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end):
        self.__end = end

    def __repr__(self):
        return "MyRange({}, {}, {})".format(self.start, self.end, self.__step)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        current = self.start
        self.start += self.__step
        return current

    def __len__(self):
        return (self.end - self.start) // self.__step

    def __getitem__(self, index):
        if index >= self.end - self.start:
            raise IndexError
        return self.start + index * self.__step

    def __reversed__(self):
        return MyRange(self.end - 1, self.start - 1, -self.__step)


r = MyRange(1, 9)
print(len(r))
print(r[2])
for i in r:
    print(i, end=' ')
for j in reversed(r):
    print(j)
