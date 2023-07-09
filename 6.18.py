def is_prime(i):
    for j in range(2, i-1):
        if i%j==0:
            return False
    return True
def condition(i,j):
    if is_prime(i) and is_prime(j):
        return True
    return False
# n = 20
# a = [[i,j] for i in range(1, n+1) for j in range(1, n+1) if is_prime(i+j) and i <= j and condition(i,j)]
# print(a)
a = [[i,i+2] for i in range(2,101) if is_prime(i) and is_prime(i+2)]
print(a)

