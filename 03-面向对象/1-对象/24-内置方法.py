#七 __setitem__,__getitem__,__delitem_  _

class FOO:
    def __init__(self,name):
        self.name=name
    #查看属性
    def __getitem__(self, item):
        print ("getitem")
        return  self.__dict__.get(item)
    #修改属性
    def __setitem__(self, key, value): #运用反射
        setattr(self,key,value)
    def __delitem__(self, key):
        delattr(self,key)
a=FOO("mazhen")
#查看属性
print (a["name"])
#修改属性
a["name"]="3333"
print (a.__dict__)
#删除属性
del a["name"]
print (a.__dict__)
#__str__方法：
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '<name:%s,age:%s>' % (self.name, self.age)


a=People("name",20)
print (a)

#__del__
# f=open('settings.py')
# f.read()
# f.close() #回收操作系统的资源

# print(f)
# f.read()
class Open:
    def __init__(self,name):
        print ("正在打开文件")
        self.name=name
    def __del__(self):
        print ("回收操作系统资源")
a=Open("hhhh")
print("程序实行完毕")

















