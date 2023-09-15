
def add(a: int, b: int) -> int:
    return a+b

# 用于静态代码检查
# cmd: mypy file.py

# c = add("s", "ss")

from typing import NewType, Callable

ID = NewType("ID", float)

def identify_id(my_id: ID):
    pass 

a = ID(3)
print(type(a))

identify_id(a)

def fun(f: Callable[[int, int], int], a, b):
    return f(a, b)

fun(add, 1, 2)