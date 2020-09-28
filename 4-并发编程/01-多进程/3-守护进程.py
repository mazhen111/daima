"""

如果我们有两个任务需要并发执行，那么开一个主进程和一个子进程分别去执行就ok了，
如果子进程的任务在主进程任务结束后就没有存在的必要了，那么该子进程应该在开启前就被设置成守护进程。主进程代码运行结束，守护进程随即终止

"""
from multiprocessing import Process
import time
import random
def task(name):
    print('%s is piaoing' % name)
    time.sleep(random.randrange(1, 3))
    print('%s is piao end' % name)
if __name__=="__main__":
    P=Process(target=task,args=("ma",))
    P.daemon=True  ##一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    P.start()
    print ("zhu") #只要终端打印出这一行内容，那么守护进程p也就跟着结束掉了

#练习题

def foo():
    print (1234)
    time.sleep(1)
    print ("end124")
def bar():
    print (456)
    time.sleep(5)
    print ("end=456")
if __name__=="__main__":
    P=Process(target=foo)
    p1=Process(target=bar)
    P.daemon=True
    P.start()
    p1.start()
    print ("主")
#思考下列代码的执行结果有可能有哪些情况？为什么？
"""
主
456
end=456

"""



