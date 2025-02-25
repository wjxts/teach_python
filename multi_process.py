# apply_async, imap

import multiprocessing as mp 
import time
# print(mp.cpu_count())

def timer(func):
    def inner_func(*args, **kwargs):
        begin = time.time()
        v = func(*args, **kwargs)
        print(f"time cost: {time.time()-begin:.3f}s")
        return v
    return inner_func

def workload(n):
    a = [n+i for i in range(2)]
    print("workload")
    return sum(a)

@timer
def normal_work(N):
    for i in range(N):
        workload(i)

@timer
def parallel_work(N):
    with mp.Pool(n_cpu) as pool:
        for i in range(N):
            pool.apply_async(workload, 
                             args=(i, ), )
                             #callback= lambda x: #print("success"), 
                             #error_callback=lambda x: print("fail"))
        pool.close()
        pool.join()

@timer
def normal_map(N):
    a = [workload(i) for i in range(N)]
    #eturn a
n_cpu = mp.cpu_count()

@timer
def parallel_map(N):
    with mp.Pool(n_cpu) as pool:
        #r = list(pool.imap(workload, range(N)))
        r = pool.imap(workload, range(N))
        #r = list(pool.map(workload, range(N)))
        #r = pool.map(workload, range(N))
        #r = pool.map_async(workload, range(N))
        # for s in r.get():
        #     pass
        print("end")
        # pool.close()
        # pool.join()
    print("final")
    #time.sleep(2)
    return r

def test_func():
    a = [i for i in range(10000)]
    print("hi")

if __name__ == "__main__":
    print(n_cpu)
    #N = 2
    #normal_work(N)
    #parallel_work(N)

    #N = 2
    #normal_map(N)
    #parallel_map(N)

    #N = 3
    #p = mp.Process(target=normal_work, args=(N, )) # not compatible with timer!
    # p = mp.Process(target=test_func)
    # p.start()
    #print("end")


    # pool = mp.Pool(n_cpu)
    # for i in range(3):
    #     pool.apply_async(test_func)
    # print("end")
    # pool.close()
    # pool.join()