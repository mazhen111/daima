import  abc
"""
多态是指一类事物有多种形态
动物有多种形态 人狗猪

"""
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def taik(self):
        pass

class People(Animal):
    def taik(self):
        print('say hello')
class Dog(Animal):
    def taik(self):
        print ('say wangwang')

"""
多态性是指在不考虑实例类型的情况下使用实例，多态性分为静态多态性和动态多态性
静态多态性：如任何类型都可以用运算符+进行运算
多态性是指在不考虑实例类型的情况下使用实例，多态性分为静态多态性和动态多态性
静态多态性：如任何类型都可以用运算符+进行运算
"""

pod=Dog()
pod.taik()

"更进一步我们确定通知接口"
def fun(obj):
    obj.taik()
fun(pod)

class Cat(Animal):
    def taik(self):
        print ("is mao")
def func (animal):
    animal.taik()

mao=Cat()
fun(mao)
"""
class Cat(Animal): #属于动物的另外一种形态：猫
...     def talk(self):
...         print('say miao')
... 
>>> def func(animal): #对于使用者来说，自己的代码根本无需改动
...     animal.talk()
... 
>>> cat1=Cat() #实例出一只猫
>>> func(cat1) #甚至连调用方式也无需改变，就能调用猫的talk功能
say miao

'''
这样我们新增了一个形态Cat，由Cat类产生的实例cat1，使用者可以在完全不需要修改自己代码的情况下。使用和人、狗、猪一样的方式调用cat1的talk方法，即func(cat1)

"""