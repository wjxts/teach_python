# 输入正整数n，返回1,2,3,..,n的连续子序列的和的所有可能值的数量
# 执行速度越快越好
def possible_sum_of_n(n):
    a = []
    for i in range(1, n+1):
        for j in range(1, i+1):
            s = 0
            for k in range(j, i+1):
                s += k
            if s not in a:
                a.append(s)
    a = sorted(a)
    #print(a)
    return len(a)

def possible_sum_of_nn(n):
    a = [sum(range(j, i+1)) for i in range(1, n+1) for j in range(1, i+1)]
    a = sorted(set(a))
    #print(a)
    return len(a)

m = 4
output1 = possible_sum_of_n(n=m)
output2 = possible_sum_of_nn(n=m)
#print(output1, output2)

def is_prime(i):
    for j in range(2, i-1):
        if i%j==0:
            return False
    return True

# a = [i for i in range(2, 20) if is_prime(i)] # list comprehension
#b = list(filter(is_prime, range(2,20))) 
#b = list(map(lambda x: x**0.5, a))\
# map, filter can be implemented by list comprehension
#b = [i**0.5 for i in a]

# def minus(x, y):
#     return x-y

# print(minus(y=2, x=1))

# from functools import reduce 
# a = [1, 2, 3]
# b = reduce(lambda x, y: [x[0]-y, x[1]+[y]], a, [10, []])

#print(a)
#print(b)