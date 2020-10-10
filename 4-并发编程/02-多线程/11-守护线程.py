"""

1、主进程在其代码结束后就已经算运行完毕了
（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，
2、主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，
而进程必须保证非守护线程都运行完毕后才能结束。


"""
from threading import  Thread
import time
# def stak(name):
#     time.sleep(2)
#     print('%s say hello' % name)
# if __name__ =="__main__":
#     t=Thread(target=stak,args=("ma",))
#     t.daemon=True
#     t.start()
#     print ("主线程")
#     print(t.is_alive())
#     time.sleep(3)

#from multiprocessing import Process

import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")

if __name__ == '__main__':
    p1=Thread(target=foo)
    p2=Thread(target=bar)

    p1.daemon=True
    p1.start()
    p2.start()
    print("main-------")
"""

123
456
main-----
end123
end456

"""