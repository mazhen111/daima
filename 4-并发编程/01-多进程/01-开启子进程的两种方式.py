from multiprocessing import Process
import time
# 第一种方法

# def tast(name):
#     print ("%s is running"%(name))
#     time.sleep(5)
#     print ("%s is done"%(name))
# if __name__=="__main__":
#     p=Process(target=tast,args=("子进程",))
#     p.start()
#     print ("主")
class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print("%s is running" % (self.name))
        time.sleep(5)
        print ("%s is done"%(self.name))

if __name__ == '__main__':
    P=MyProcess("MAZHEN")
    P.start()
print ("主进程")
