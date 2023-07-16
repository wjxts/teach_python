# apply_async, imap

import multiprocessing as mp 
from time import time 
# print(mp.cpu_count())
n_cpu = mp.cpu_count()


def timer(func):
    def inner_func(*args, **kwargs):
        begin = time()
        v = func(*args, **kwargs)
        print(f"time cost: {time()-begin:.3f}s")
        return v
    return inner_func

def workload(n):
    return [n+i for i in range(1000)]

# @timer
# def normal_work(N):
#     for i in range(N):
#         workload(i)

# @timer
# def parallel_work(N):
#     with mp.Pool(2) as pool:
#         for i in range(N):
#             pool.apply_async(workload, 
#                              args=(i, ), 
#                              callback=lambda x: print("success"), 
#                              error_callback=lambda x: print("fail"))
        # pool.close()
        # pool.join()
# N = 2
# normal_work(N)
# parallel_work(N)
@timer
def normal_map(N):
    a = [workload(i) for i in range(N)]
    return a

@timer
def parallel_map(N):
    with mp.Pool(n_cpu-3) as pool:
        r = list(pool.imap(workload, range(N)))
    return r

N = 100
#normal_map(N)
parallel_map(N)