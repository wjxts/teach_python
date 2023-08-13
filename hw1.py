# 实现一个函数，输入一个正整数n，返回1+2+...+n
def sum_1(n):
    c = 0
    for i in range(1,n+1):
        c = i + c 
    return c 

output = sum_1(5)
print(output)
exit(2)