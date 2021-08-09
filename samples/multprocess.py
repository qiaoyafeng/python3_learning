from multiprocessing import Process, Queue
import os, time, random

# 写入数据 进程
def write(q):
    print('Process %s is writing...' % os.getpid())
    values = ['A', 'B', 'C', 'D']
    for value in values:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读取数据 进程
def read(q):
    print('Process %s is readding...' % os.getpid())
    while True:
        value = q.get()
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    # 父进程创建Queue传递给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动写入的子进程
    pw.start()
    # 启动读取的子进程
    pr.start()
    # 等待写入子进程结束
    pw.join()
    # 读取子程序为无限循环，只能强制终止
    pr.terminate()