"""
exec
#参数1 字符串形式的命令
参数2 全局作用域(字典的形式)如果不指定默认就使用glabals()
参数3 局部作用域（字典的形式）如果不指定默认就使用locals()
"""
# g = {
#     "x":1,
#     "y":2
#
# }
# l={}
#
# exec (
# """
# global x,m
# x=10
# y=20
# z=3
#
# """,g,l)
# print (g)
# print (l)
"""
一切皆对象，对象可以怎么用
1 都可以被引用，x=obj
2 都可以当做函数的参数传入
3 都可以当做函数的返回值
4 都可以当做容器类的元素 l=[func,time,obj,1]

"""
#类也是对象,Foo=type(....)
class Foo:
    pass
print (type(Foo))
a=Foo()
print (type(a))

#产生类的类称之为元类，默认所以用class定义的类，他们的元类是type
#类定义的两种方式
class Foo:
    def __init__(self,name):
        self.name=name
    def run(self):
        print ('%s is talking' %self.name)
test=Foo("mazhen")
test.run()
#第二种方式 type

#定义类的三要素类名 类的，类的父类 类体
#类的
class_name="Chinses"
#类的父类
class_bass=(object,)
class_iboy="""
def __init__(self,name):
    self.name=name
def run(self):
    print ('%s is talking no' %self.name)

"""
class_dir={}
exec (class_iboy,globals(),class_dir)
# print (class_dir)
Chinese1=type(class_name,class_bass,class_dir)
a=Chinese1("mazhen")
a.run()