#储备知识_call__方法
# class Foo:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self, *args, **kwargs):
#         print (self)
#         print (args)
#         print (kwargs)
# a=Foo("nmae")
# a(1,2,3,4)
class mate(type) :
    def __init__(self,class_name,class_bases,class_dic):
        print (class_dic)
        if not class_name.istitle():
            raise TabError("类名首字母必须大写")
        if "__doc__" not in class_dic or not class_dic["__doc__"].strip():
            raise TabError("必须有注释，且注释不能为空")
        super(mate,self).__init__(class_name,class_bases,class_dic)
        def __call__(self, *args, **kwargs):
            #第一件事情先造一个空间
            obj=object.__new__(self)
            print (args)
            self.__init__(obj,*args,**kwargs)
            return obj



class Chinses(object,metaclass=mate):
    """
    mazhen
    """
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        print ("mamama%s"%(self.name))
a=Chinses("mazhen",age=18)