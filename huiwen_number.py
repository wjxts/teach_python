def is_huiwen(n):
    '''
    input n: a natural number (n>0)
    return True is n is huiwen number, False otherwise
    '''
    y = str(n)
    if y[::-1] == y:
        return True
    return False
    # if y[::-1] == y:
    #     return True
    # else:
    #     return False
    # return str(n)[::-1] == str(n)

# you need to implement function is_huiwen

x = is_huiwen(123)
print(x)
x = is_huiwen(131)
print(x)
x = is_huiwen(3443)
print(x)

# you need to compute the number of huiwen numver in 1~10000
cnt = 0
for i in range(10000,20001):
    if is_huiwen(i):
        # print(i)
        cnt += 1
print(cnt)