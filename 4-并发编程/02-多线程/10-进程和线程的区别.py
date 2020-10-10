from threading import Thread
from multiprocessing import Process
import time
import os

#1、开进程的开销远大于开线程
# def piao(name):
#     print('%s piaoing' %name)
#     time.sleep(2)
#     print('%s piao end' %name)
#
# if __name__ == '__main__':
#     p1=Process(target=piao,args=('egon',))
#     p1.start()
#
#     # t1=Thread(target=piao,args=('egon',))
#     # t1.start()
#     print('主线程')

#2、同一进程内的多个线程共享该进程的地址空间
n=100
def piao(name):
    global n
    n=10

if __name__ == '__main__':
    # p1=Process(target=piao,args=('egon',))
    # p1.start()

    t1=Thread(target=piao,args=('egon',))
    t1.start()
    print('主线程',n)
#3、瞅一眼线程的pid相同
# def task():
#     # print(current_process().pid)
#     print('子进程PID:%s  父进程的PID:%s' %(os.getpid(),os.getppid()))
#
# if __name__ == '__main__':
#     p1=Process(target=task,)
#     p1.start()
#
#     # print('主线程',current_process().pid)
#     print('主线程',os.getpid())
#线程
def task():
    # print(current_process().pid)
    print('子进程PID:%s' %(os.getpid()))

if __name__ == '__main__':
    t1=Thread(target=task,)
    t1.start()

    # print('主线程',current_process().pid)
    print('主线程',os.getpid())