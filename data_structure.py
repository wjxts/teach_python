# 数据结构及其操作 (构造、方法、转化、遍历)

# list 列表
# a = [] # 空列表
# a = [l1, l2, l3, ...]

a = [1, 'monday', True, 3.14]
b = ['car', 2.1]
#c = a[0:2] + b + a[2:]

# 遍历
# for item in a:
#     print(item)

# 向末尾添加一个元素
# a.append(10)
# print(a)
# a = a.append(10) is wrong!!!

# 在某个位置插入一个元素
# a.insert(0, 10) #a.insert(index, value)
# print(a)

# 弹出末尾元素
# v = a.pop() 
# print(a, v)
# can be a.pop(index)

# 拼接
# c = a + b 
# a.extend(b)
# print(c, a, sep='\n')

# 索引
# print(a[1])

# 切片 (逻辑与str基本相同）（返回一个list）
# print(a[1:3], a[3:1:-1])

# 判断元素是否存在
# j = 1 in a
# jj = 2 in a 
# print(j, jj)

# 查找位置
# print(a.index('monday'))


## dict 

# def func():
#     pass 
# a = (1, 2)
# d = {1: 'monday', 2: 'tuesday', 'name': 'zz', 'age': 10, func: 1, a: 2}
# print(d)
# print(d[a])

d = {} # 空字典
# print(d)
d['today'] = 2
#print(d)
d['today'] = 3
#print(d)
d['tomorrow'] = 3
#print(d)
dd = {"next day":4, 'today':5}
d.update(dd)
#print(d)

# from collections import OrderedDict

# 遍历
# for k, v in d.items():
#     print(k, v)

# for item in d.items():
#     k, v = item
#     print(item, k, v)

# keys = list(d.keys())
# print(keys)
# values = list(d.values())
# print(values)

# for key in d.keys():
#     print(key, d[key])

# list和dict相互转化
# print(d)
#a = list(d) # 只获取key, 等价于 list(d.keys())
# dd = dict(a) # 会报错！
#print(a)
# b = list(d.items())
# print(b)
# dd = dict(b)
# print(dd)

#a = [[2, True], [3, True], [4, False]]
#a = [(2, True), (3, True), (4, False)]
#a = [(2, True), [3, True], [4, False]]
# dd = dict(a)
# print(dd)

#d['tod']
#v = d.get('tod', 2)
#print(v)

# try:
#     v = d['tod']
# except:
#     print("key not in dict!")
#     v = 2
# print(v)

# tuple #就是不可修改的List
# a = ()
# print(type(a))
# a = (1)
# print(type(a))
# a = (1, )
# print(type(a))
# a = (1, 2)
# print(type(a))
# print((1, 2), (1, 2,))

# a = [1, 2, 3]
# b = tuple(a)
# b[1] = 3 #会报错， tuple不能对元素赋值
# c = list(b)
# print(b, c)

# def func(x):
#     return x+3, x**2

# y = func(2)
# print(y)
# y1, y2 = func(2)
# print(y1, y2)

# f = lambda x: (x+3, x**2)
# y = f(2)
# print(y)

# a = (1, 2, 5, 6, 7)
# print(len(a), a[2:4], a[1], a.index(2))
# print(a + (1,2))


# set 
# a = set()
# print(type(a))

# a = {1, 2, 1, 3, 2, 1}
# print(a)

# 可用于列表或元组去重
# a = [1, 2, 1, 3, 2, 1]
# b = set(a)
# print(b)
# a = list(b)
# print(a)

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# print(a | b)
# print(a & b)
# print(a - b)
# print(a ^ b)
# a.add(5)
# print(a)
# a.remove(2)
# print(a)

# from collections import Counter 

# a =  [1, 2, 1, 3, 2, 1]
# c = Counter(a)
# print(c)
# print(c[1])
# print(c.most_common(1))

# c.update([1])
# c.update({4: 2, 1: 2})
# c.update(['zz','ss','zz'])
# print(c)
