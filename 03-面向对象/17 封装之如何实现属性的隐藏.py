"""
封装其实这仅仅这是一种变形操作
类中所有双下划线开头的名称如__x都会变形成_类的名称__x
"""

"""
类中定义的__X只能再内部使用例如seif.__X,引用就是变形的结果
这种变形其实正是针对外部的变形，再外部是无法通过__X访问到的
再子类定义的__X不会覆盖在父类定义的__X以为自雷中行程了_子类名_x而父类形成的_父类名__X即双下划线开头的属性在继承给子类时子类时无法覆盖的

"""
# class A:
#     __N=0
#     def __init__(self):
#         self__N=0 #变形为self._A__N
#     def __foo(self):
#         print ("from A")
#     def bar(self):
#         self.__foo()
# a=A()
# a._A__foo()
# print (A .__dict__)
"""  '_A__N': 0, A__foo'"""

#问题3  再子类定义的__X不会覆盖在父类定义的__X以为自雷中行程了_子类名_x而父类形成的_父类名__X即双下划线开头的属性在继承给子类时子类时无法覆盖的
class A:
    def __foo(self):
        print ("A.foo")
    def bran(self):
        print('A.bar')
        self.__foo() #Self._A__foo
class B(A):
    def __foo(self):
        print ("b.foo")
foo=B()
foo.bran()
"""A.bar
A.foo
"""
"""
1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以拼出名字：_类名__属性，然后就可以访问了，如a._A__N
2、变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
"""
A.__C=4
print (A.__dict__)
"""  '__C': 4"""
