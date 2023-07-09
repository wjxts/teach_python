# data type and operation

# basic data type
a = 1 # int
b = 1.0 # float
c = True # bool
s = "ysz" # str

# type(s)

# transformation between data type (数据类型转换)
s1 = "123" 
a1 = int(s1)

s2 = str(a1)

# basic operation


# float/int +, -, *, /, **
# 1.5e2
# int //, %  a = (a//b)*b+a%b

# bool and, or, not, ==, !=, >, <, >=, <=

# string +, index & slice (start from 0) [3]; [-3]; [:3]; [:-1]; [:]; s[m:n] include m, not include n; s[m:n:-1] 
# len(s)
## find s1.find(s2), "whatever".find('ever') return 4;  "whatever".find('wever') return -1
# format (格式化) ,  f"a = {a}, b = {b}", "a = {}, b = {}".format(a, b), "a = {a}, b = {b}".format(a=a, b=b)
## c = ["monday", "tuesday", "holiday"], " ".join(c)
## s.upper(), s.lower(),  s.isupper(),  s.islower()

## s1 = "monday";  s1 = s1[0].upper() + s1[1:]
## s1 + "+" + s2, f"{s1}+{s2}" ,"+".join([s1, s2])
