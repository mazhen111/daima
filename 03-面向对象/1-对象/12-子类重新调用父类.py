"""
在子类派生出的新方法中，往往需要重用父类的方法，我们有两种方式实现
方式一：指名道姓，即父类名.父类方法()
"""
# class Vehicle:
#     def __init__(self,name,speed,load,power):
#         self.name=name
#         self.speed=speed
#         self.load=load
#         self.power=power
#     def run(self):
#         print('开动啦...')
# class Subway(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         Vehicle.__init__(self,name,speed,load,power)
#         self.line=line
# c=Subway('中国地铁','180m/s','1000人/箱','电',13)
# print (c.__dict__)
# c.run()

"""
第二种方式 super()
"""
# class Vehicle:
#     def __init__(self,name,speed,load,power):
#         self.name=name
#         self.speed=speed
#         self.load=load
#         self.power=power
#     def run(self):
#         print('开动啦...')
# class Subway(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         super().__init__(name,speed,load,power)
#         self.line=line
# c=Subway('中国地铁','180m/s','1000人/箱','电',13)
# print (c.__dict__)
# c.run()

"""
这两种方式的区别是：方式一是跟继承没有关系的，而方式二的super()是依赖于继承的，并且即使没有直接继承关系，super仍然会按照mro继续往后查找

"""

class A:
    def test(self):
        super().test()
class B:
    def test(self):
        print('from B')
class C(A,B):
    pass
c = C()
print (C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
c.test()


