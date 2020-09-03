# 反射：通过字符串映射到对象的属性
class  people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def talk(self):
        print('%s is talking' % self.name)

obj=people("mazhen",12)
obj.talk()
#hasattr 判断object中有没有一个name字符串对应的方法或属性
print(hasattr(obj,"name"))
"""
False
"""
##获取属性 getattr
print (getattr(obj,"name"))

#修改属性
setattr(obj,"name","20")
print (obj.__dict__)

delattr(obj,"name")

#反射的作用
class sevice:
    def run(self):
        name=input("请输入启动的模块").strip()
        cmd = name.split()
        if hasattr(self,cmd[0]):
            ftun=getattr(self,cmd[0])
            ftun(cmd)
    def get(self,cmd):
        print ('get.......',cmd)
    def put(self,cmd):
        print ('get.......',cmd)
a=sevice()
a.run()