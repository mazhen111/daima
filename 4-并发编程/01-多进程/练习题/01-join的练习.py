from multiprocessing import Process
import time
import random
#效果一：保证最先输出-------->4
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     print('-------->4')

#保证最后输出-------->4
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     print('-------->4')

#效果三：保证按顺序输出
# def task(n):
#     time.sleep(random.randint(1,3))
#     print('-------->%s' %n)
#
# if __name__ == '__main__':
#     p1=Process(target=task,args=(1,))
#     p2=Process(target=task,args=(2,))
#     p3=Process(target=task,args=(3,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()
#     print('-------->4')



