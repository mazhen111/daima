from  threading import Thread,Lock
import time


n=100

def take():
    global n
    l.acquire()
    temp=n
    time.sleep(0.6)
    n=temp-1
    l.release()
if __name__ == '__main__':
    l=Lock()
    list = []
    for i in range(100):
        p=Thread(target=take)
        list.append(p)
        p.start()
    for a in list:
        a.join()
    print ("主",n)

