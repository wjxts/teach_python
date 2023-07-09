import numpy as np 

np.random.seed(1)

a1 = np.zeros([2,3])
a2 = np.ones([2,3])
a3 = np.random.randn(2, 3)
a4 = np.random.rand(2, 3)
a5 = np.random.randint(0, 10, size=(2, 3))
# print(a[1, 2])
# print(a[1:3, :2].shape)
# print(a1, a2, a3, a4, a5, sep="\n")

a = np.zeros([4, 4], dtype=int)
# a[2, 3] = 1
# print(a)

# b = np.random.randint(0, 10)
# print(b)
# a[1] += 1

def is_legal(a,i,j):
    pass 
