# file = "E:\learn_python\output.txt"
file = "output.txt"
# file = r"D:\ysz\files\123.txt"
# with open(file, 'r') as f:
#     s = f.read()
#     # lines = f.readlines()
# print(s)
# file_out = "out.txt"
# with open(file_out, 'w') as f:
#     f.write("\n")
#     f.write(s + "111HAHA")

# with open(file_out, 'a+') as f:
#     f.write("\n")
#     f.write(s + "111HAHA")

# from time import time
# class Timer:
#     def __enter__(self):
#         print("begin timer")
#         self.begin = time()
#         print(self.begin)
#         return self 
    
#     def __exit__(self, type, value, trace):
#         print("end timer")
#         print(f"time cost: {time()-self.begin:.3f}s")
#         return 

# with Timer() as t:
#     for i in range(1000000):
#         a = i**2

# Decorator (grammar sugar)
# from time import time

# def timer(func):
#     def inner_func(*args, **kwargs):
#         begin = time()
#         v = func(*args, **kwargs)
#         print(f"time cost: {time()-begin:.3f}s")
#         return v
#     return inner_func

# def named_timer(name):
#     def timer(func):
#         def inner_func(*args, **kwargs):
#             begin = time()
#             v = func(*args, **kwargs)
#             print(f"{name} time cost: {time()-begin:.3f}s")
#             return v
#         return inner_func
#     return timer

#@timer
#func=timer(func)

# @timer
# @named_timer("fengtai")
# def loop():
#     for i in range(1000000):
#         a = i**2
# loop()

# REGISTRY = {}
# def register_class(name):
#     def register(cls):
#         REGISTRY[name] = cls 
#         return cls
#     return register

# def build_class(name):
#     return REGISTRY[name]

# @register_class('A')
# class A:
#     pass 

# @register_class('B')
# class B:
#     pass 

# print(REGISTRY)
# name = "A"
# a = build_class('A')
# print(a)

# import json 

# d = {"a":1, "b":2}
# file = "tem.json"
# json.dump(d, open(file, 'w'), indent=2)
# td = json.load(open(file, 'r'))
# print(td)

# from util import fun 
# import util
# util.fun(2)
from new_math.util import fun as f
f(2)

