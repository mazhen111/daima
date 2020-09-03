import  settings
import hashlib
import time
class People:
    def __init__(self,name,age,sex):
        self.id = self.create_id()
        self.name=name
        self.age=age
        self.sex=sex
    def tell_info(self):
        print ('Name:%s Age:%s Sex:%s id:%s' %(self.name,self.age,self.sex,self.id))
    @classmethod
    def from_conf(cls):
        obj=cls(
            settings.name,
            settings.age,
            settings.sex
        )
        return obj
    @staticmethod
    def create_id():
        m=hashlib.md5(str(time.time()).encode("utf-8"))
        return m.hexdigest()

# p=People('egon',18,'male')

#绑定给对象，就应该由对象来调用，自动将对象本身当作第一个参数传入
# p.tell_info() #tell_info(p)

#绑定给类，就应该由类来调用，自动将类本身当作第一个参数传入
# p=People.from_conf() #from_conf(People)
# p.tell_info()
test=People("nazhen",20,40)
test.tell_info()
p=People.from_conf()
p.tell_info()
a=People("mazhen",30,"40")
a.tell_info()
