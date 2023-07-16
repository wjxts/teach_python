# Iterable, Iterator, generator

# a = [1, 2, 3]
# for i in a:
#     print(i)

class MyIter:
    def __init__(self, n) -> None:
        self.n = n
        self.cur = 0
    
    def __next__(self):
        if self.cur < self.n:
            self.cur += 1
            return self.cur
        else:
            self.cur = 0
            raise StopIteration
        
    def __iter__(self):
        return self

class MyIterable:
    def __init__(self, n) -> None:
        self.it = MyIter(n)
    def __iter__(self):
        return self.it

# myiter = MyIter(3)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# for i in myiter:
#     print(i)
# for i in myiter:
#     print(i)

# myiterable = MyIterable(3)
# for i in myiterable:
#     print(i)

# def gen(n):
#     i = 1
#     while i<=n:
#         print("g",i)
#         yield i
#         i = i+1

# g = gen(3)
# for i in g:
#     print(i)


def gen(n):
    i = 1
    while i<=n:
        # print("g",i)
        r = yield i
        if r is not None:
            i = r
        i = i+1

g = gen(10)
print(next(g))
print(g.send(5))
print("-"*10)
for i in g:
    print(i)