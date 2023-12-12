# def is_huiwen(s: str) -> bool:
#     return s[::-1] == s
# is_huiwen = lambda s: s == s[::-1]

# s_list = ['12321', '1232', 'asadr', 'appa']
# for s in s_list:
#     print(is_huiwen(s))
# from collections import Counter

# c1 = Counter('gallahad')
# c2 = Counter('gall')
# add = lambda a, b: a + b
# print(add(c1, c2))
# a = '-1243151'
# # b = list(a)
# print(a.find('124'))
# print([chr(ord('a')+i) for i in range(26)])
fun1 = lambda x:(x, x+1)
def fun2(x):
    return x, x+1

print(fun1(1),fun2(1))