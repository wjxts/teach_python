import numpy as np
from time import time 
# (f_n+1, f_n)^T = [[1, 1], [1, 0]](f_n, f_n-1)^T
A = np.array([[1, 1], [1, 0]])
MOD = 100000
def fib0(a, b, n):
    while n>0:
        a, b = b % MOD, (a+b) % MOD
        n -= 1
    return a

def fib(a, b, n):
    if n==0:
        return a 
    if n==1:
        return b 
    bin_s = bin(n)[2:]
    An = [A]
    for _ in range(len(bin_s)-1):
        An.append(An[-1]@An[-1] % MOD)
    final_A = np.eye(2)
    for i, c in enumerate(bin_s[::-1]):
        if c=='1':
            final_A = final_A@An[i] % MOD
    init_vec = np.array([[a],[b]])
    final_vec = final_A@init_vec % MOD
    return round(final_vec[1][0])

# a = b = 1
# n = 1000000
# tik = time()
# print(fib0(a, b, n))
# tok = time()
# print(f"{tok-tik:.2f}")
# tik = time()
# print(fib(a, b, n))
# tok = time()
# print(f"{tok-tik:.2f}")
    
# 判断一个数是否在斐波那契数列中 

def in_seq(a, b, target):
    if a==target:
        return True 
    if a*b<0:
        # 异号
        a, b = a+b, a 
    else:
        pass 
    
    