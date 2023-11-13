class A:
    def fun(self, x):
        print(f"fun of A called with {x}")


def sad(self, x):
    print(f"sad of A called with {x}")
    self.fun(x)
    
    
a = A()
a.fun(1)
a.sad = sad 
a.sad(a, 2)
