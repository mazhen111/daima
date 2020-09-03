"""
单实例模式
"""
#第一种方式实现
class Mysql:
     __instance=None
     print (__instance)
     def __init__(self):
          self.host='127.0.0.1'
          self.port=3306
     @classmethod
     def singleton(cls):
         if not cls.__instance:
             obj=cls()
             print ("mamam")
             cls.__instance=obj
         return cls.__instance

     def conn(self):
         pass

obj1 = Mysql.singleton()
obj2=Mysql.singleton()
obj3=Mysql.singleton()

# obj1=Mysql()
# obj2=Mysql()
# obj3=Mysql()
print(obj1)
print(obj2)
print(obj3)
class mate(type) :
    def __init__(self,class_name,class_bases,class_dic):
        print (class_dic)
        if not class_name.istitle():
            raise TabError("类名首字母必须大写")
        if "__doc__" not in class_dic or not class_dic["__doc__"].strip():
            raise TabError("必须有注释，且注释不能为空")
        super(mate,self).__init__(class_name,class_bases,class_dic)
        __instance = None
        def __call__(self, *args, **kwargs):
            if not self.__instance:
                #第一件事情先造一个空间
                obj=object.__new__(self)
                print (args)
                self.__init__(obj,*args,**kwargs)
                self.__instance=obj
                return self.__instance


class Mysql(metaclass=mate):
    __instance = None
    print(__instance)

    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 3306




