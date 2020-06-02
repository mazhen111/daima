def consumer(name):
    print ("%s准备吃包子"%name)
    while True :
        baozi = yield
        print ("包子[%s]来了,被[%s]吃了!" %(baozi,name))
c = consumer("A")
c1 = consumer("B")
c2 = consumer("C")
c.__next__()
c1.__next__()
c2.__next__()
print("----老子开始准备做包子啦!----")
for i in range(1000000):
    c.send(i)
    c1.send(i)
    c2.send(i)


