import json,time
from multiprocessing import Process,Lock
def search(name):
    time.sleep(1)
    dic=json.load(open("date","r",encoding="utf-8"))
    print('<%s> 查看到剩余票数【%s】' % (name, dic['count']))
def get(name):
    time.sleep(2)
    dic=json.load(open("date","r",encoding="utf-8"))
    if dic["count"] >0:
        dic["count"]-=1
        time.sleep(3)
        json.dump(dic,open("date","w",encoding="utf-8"))
        print('<%s> 购票成功' % name)

def task(name,musk):
    search(name)
    musk.acquire()
    get(name)
    musk.release()
if __name__=="__main__":
    musk = Lock()
    for i in range(10):
        p=Process(target=task,args=('路人%s' %i,musk))
        p.start()

