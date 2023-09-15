class A:
    def __init__(self) -> None:
        self.x = 1
        self.fun()
        super().fun() # C.fun(self)

    def fun(self):
        print("A here")

class B(A):
    b = 1
    def __init__(self) -> None:
        self.fun()
        super().__init__()
        

    def fun(self):
        print("B here")

class C:
    b = 2
    def __init__(self) -> None:
        self.c = 3
        self.fun()

    def fun(self):
        print(self)
        print("C here")

class D(B, C):
    def __init__(self) -> None:
        # super().__init__()  # super(D, self).__init__(), B.__init__(self)
        #A.__init__(self)
        pass 

    def fun(self):
        print("D here")
    
    def __str__(self):
        return "member D"


print(D.mro())
# method resolution order
d = D()
print(d.b)

# 继承的是属于类的东西, 类的变量和方法