import multiprocessing
import time
from collections import deque 

# 定义要在新进程中运行的任务
def task(name, q):
    print(f"Process {name} is starting...")
    time.sleep(1)  # 模拟长时间运行的任务
    print(f"Process {name} is finished.")
    q.put(name)  # 将进程名字放入队列
    # return name

def run_task(task, name, q):
    task(name, q)
    
if __name__ == "__main__":
    print("Main process is starting...")
    begin_time = time.time()
    # 创建进程列表
    processes = []
    # 启动多个进程
    q = multiprocessing.Queue()
    
    
    task_queue = deque([1])
    index = 1
    while task_queue:
        processes = []
        while task_queue:
            task_id = task_queue.popleft()
            process = multiprocessing.Process(target=run_task, args=(task, f'Process-{task_id}', q))
            processes.append(process)
            process.start()
        for process in processes:
            process.join()
        index += 1
        if index <= 4:
            task_queue.append(index)
        else:
            break
        
        
       
        
    # 写一个最简单的依赖, 1->2->3->4
    # for i in range(4):
    #     # process = multiprocessing.Process(target=task, args=(f'Process-{i}',q))
    #     process = multiprocessing.Process(target=run_task, args=(task, f'Process-{i}', q))
    #     processes.append(process)
    #     process.start()

    # 等待所有进程完成
    # for process in processes:
    #     process.join()
    # 打印queue中的内容
    while not q.empty():
        print(q.get())
    print("All processes are finished.")
    end_time = time.time()
    print(f"Total time: {end_time - begin_time:.2f} seconds.")
