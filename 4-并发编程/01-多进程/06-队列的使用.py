from  multiprocessing import Queue
q=Queue(3)
q.put("11")
q.put("333")
q.put(["2222"])
print (q.full())#查看是否满
#q.put(444)
print (q.get())
print (q.get())
print (q.get())
print(q.empty()) #查看是否拿空
print (q.get())