#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import queue
from multiprocessing.managers import BaseManager

# 发送任务队列
def task_queue():
    task_queue = queue.Queue()
    return task_queue
# 接收结果队列
def result_queue():
    result_queue = queue.Queue()
    return result_queue

# 从BaseManager继承的QueueManager
class QueruManager(BaseManager):
    pass

# 把两个队列都注册到网络上，callable关联了Queue对象
QueruManager.register('get_task_queue', callable=task_queue)
QueruManager.register('get_result_queue', callable=result_queue)
# 绑定端口 5000 ，设置验证码 'abc'
manager = QueruManager(address=('', 8888), authkey=b'abc')
print('Manager=',manager)
# 启动Queue
manager.start()
# 获取通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
print('Task=',task)
print('Result=',result)
# 添加任务
for i in range(10):
    n = random.randint(1, 500)
    print('Put task %d' %n)
    task.put(n)

print('Get results...')

# 从接收队列获取结果
for i in range(10):
    r = result.get(timeout=10)
    print('Get result %d' %r)

# 关闭管理器
manager.shutdown()
print('Master exit.')


