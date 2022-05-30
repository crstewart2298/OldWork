class Counter:
    def __init__(self):
        self.__count = 0


    def increment(self):
        self.__count += 1
        

    @property
    def count(self):
        return self.__count
a = Counter()
b = Counter()
print(a.count)
print(b.count)
a.increment()
print(a.count)
print(b.count)
a.increment()
a.increment()
b.increment()
print(a.count)
print(b.count)
