from multiprocessing import Process
import  time,os
def task():
    print ("%sin runnis 父进程%s"%(os.getpid(),os.getppid()))
    time.sleep(3)
    print("%sin done父进程id%s" %(os.getpid(),os.getppid()))
if __name__=="__main__":
    p=Process(target=task)
    p.start()
print ("主",os.getpid())