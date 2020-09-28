from  multiprocessing import  Process ,JoinableQueue
import time
def producer(q,name):
    for i in range(10):
        res="%s包子%s"%(name,i)
        time.sleep(0.3)
        print ('生产者生产了%s' %res)
        q.put(res)
    q.join()
def consumer(q):
    while True:
        res=q.get()
        if res ==None:break
        time.sleep(1)
        print('消费者吃了%s' % res)
        q.task_done()
if __name__== "__main__":
    q=JoinableQueue()
    #s生产者
    p=Process(target=producer,args=(q,"白菜"))
    p1 = Process(target=producer, args=(q,"肉"))
    p2 = Process(target=producer, args=(q,"臭豆腐"))
    #消费者
    c=Process(target=consumer,args=(q,))
    c2 = Process(target=consumer, args=(q,))
    c.daemon=True
    c2.daemon=True
    p.start()
    p1.start()
    p2.start()
    c.start()
    c2.start()
    p.join()
    p1.join()
    p2.join()
    print("主")