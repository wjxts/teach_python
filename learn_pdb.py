def g(x):
    return x**2

def f(n):
    # breakpoint()
    res = [10]
    for i in range(n):
        res.append(g(i))
    # breakpoint()
    return res

if __name__ == "__main__":
    print(f(3))