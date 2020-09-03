"""
在类内部定义的函数，分为两大类
1 是绑定方法，绑定给谁，应该有谁来调用，谁来调用就把谁当作第一参数自动传入
绑定到对象的方法：在类定义的没有任何装饰器
绑定到类的方法：在类内定义的被装饰器classmethod修饰的方法
2 非绑定方法：没有自动传值这么一说，就类中定义的一个普通工具，对象和类都可以使用
非绑定方法不与类或者对象绑定
"""
class FOO:
    def __init__(self,name):
        self.name=name
    def tell(self):
        print (self.name) #绑定对象
    @classmethod
    def func(cls):
        print (cls) #绑定到类
    @staticmethod
    def jisuan(x,y):
        print (x*y)
a=FOO("mazhen")
a.tell()
FOO.func()
a.jisuan(60,30)