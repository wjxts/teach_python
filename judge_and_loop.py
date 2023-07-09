'''
expre = True

if expre:
    print(1)
else:
    print(2)

if not expre:
    print(1)
elif False:
    print(2)
elif False:
    print(3)
else:
    print(4)

a = 3

b = 2 if a != 3 else 3
print(b)

a = -10
b = -a if a < 0 else a
print(b)
'''


# for item in iterator:
#     ...
ss = ""
for s in ['mon', 'tue','wed']:
    ss += s # equi to ss = ss + s
    ss += "0"

ss = ss.strip("0")
# print(ss, s, sep='\n') 

# for item in ['mon', 1, ['tues', 2, ['wed', 3]]]:
#     print(item, end=' ')
# print()

# for i in range(10): # equi to range(0, 10)
#     print(i, end=" ")
#     # print(i, end=" ", file=open("output.txt", 'a+'))
# print()

# for i in range(10, 20):  # (begin, end) , equi [begin, begin+1, ..., end-1], not include end
#     print(i, end=" ")
# print()

# for i in range(10, 20, 3): # (begin, end, step) , equi [begin, begin+step, ...], not include end
#     print(i, end=" ")
# print()

# for i in range(10, 20): # print the number in [10, 20) that is divided by 5
#     if i % 5==0:
#         print(i, end=' ')
# print()
i = 0
s = 0
while i<=10:
    i += 1
    s += i
print(s)