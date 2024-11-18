import multiprocessing
import time

# 定义要在新进程中运行的任务
def task(name, q):
    print(f"Process {name} is starting...")
    time.sleep(2)  # 模拟长时间运行的任务
    print(f"Process {name} is finished.")
    q.put(name)  # 将进程名字放入队列
    # return name

if __name__ == "__main__":
    print("Main process is starting...")
    begin_time = time.time()
    # 创建进程列表
    processes = []
    # 启动多个进程
    q = multiprocessing.Queue()
    for i in range(5):
        process = multiprocessing.Process(target=task, args=(f'Process-{i}',q))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()
    # 打印queue中的内容
    while not q.empty():
        print(q.get())
    print("All processes are finished.")
    end_time = time.time()
    print(f"Total time: {end_time - begin_time:.2f} seconds.")
