from types import SimpleNamespace

# 定义一个字典
my_dict = {'a': 1, 'b': 2, 'c': 3}

# 将字典转换成命名空间对象
my_namespace = SimpleNamespace(**my_dict)

# 现在可以使用点符号（.）访问命名空间的属性
print(my_namespace.a)  # 输出: 1
print(my_namespace.b)  # 输出: 2
print(my_namespace.c)  # 输出: 3