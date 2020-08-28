"""
python程序员通常根据这种行为来编写程序。例如，如果想编写现有对象的自定义版本，可以继承该对象

也可以创建一个外观和行为像，但与它无任何关系的全新对象，后者通常用于保存程序组件的松耦合度

"""
class Txtfine:
    def read(self):
        pass
    def write(self):
        pass
class DiskFile:
    def read(self):
        pass
    def write(self):
        pass
#例2：序列类型有多种形态：字符串，列表，元组，但他们直接没有直接的继承关系
s=str("hello")
l=list([1,2,3])
t=tuple((4,5,6))
print (len(l))