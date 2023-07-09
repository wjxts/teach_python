def god(a, b): # 使代码模块化，功能清晰，并且可以复用
    c = a * b 
    return c

# c = god(1, 2)
# print(c)

# c = god('hhs', 3) # 将字符串复制3次
# print(c)

def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True

# cnt = 0
# for i in range(2, 101):
#     if is_prime(i):
#         print(i, end=" ")
#         cnt += 1
# print()
# print("# of prime in 1~100: {}".format(cnt))

def factorial(n):
    c = n
    for i in range(0,n-1):
        c = c *(n-i-1)
    return c

def simple_factorial(n):
    c = 1
    for i in range(1, n+1):
        c = c*i 
    return c

# out = simple_factorial(6)
# print(out)

def func_name(a, b, c):
    if a>0:
        return b+c 
    else:
        return a+b 

# lambda表达式 方便、简洁、紧凑
# f = lambda x, y: x+y 
# print(f(1, 2))

# 内置函数
a = [2, -30, 23, -12, 0, 32]
# print(min(a), max(a), len(a), sum(a), sum(a)/len(a))
# b = sorted(a)
# c = sorted(a, reverse=True)
# d = sorted(a, key=abs)
# print(a, b, c, d, sep='\n')

# ss = ['hat', 'book', 'bi', 'numvber', 'bibz']
# s1 = sorted(ss)
# s2 = sorted(ss, key=len)
# s3 = sorted(ss, key=lambda x: x[-1:])
# print(ss, s1, s2, s3, sep='\n')

# try:
#     import torch
#     print("exist torch")
# except:
#     print("no torch package")

# a = 2
# b = 2
# try:
#     c = a / b
# except:
#     print(f"{a} can't be devided {b}")
#     c = a 

# print(c)