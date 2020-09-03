"""
python到底是如何实现继承的，对于你定义的每一个类，python会计算出一个方法解析顺序(MRO)列表，这个MRO列表就是一个简单的所有基类的线性顺序列表
在Java和C#中子类只能继承一个父类，而Python中子类可以同时继承多个父类，如果继承了多个父类，那么属性的查找方式有两种，分别是：深度优先和广度优先
"""

class A(object):
    def test(self):
        print('from A')

class B(A):
    # def test(self):
    #     print('from B')
    pass

class C(A):
    def test(self):
        print('from C')

class D(B):
    # def test(self):
    #     print('from D')
    pass

class E(C):
    def test(self):
        print('from E')

class F(D,E):
     #def test(self):
      #   print('from F')
      pass
a=F()
a.test()
print (F.mro()) #只有新式才有这个属性可以查看线性列表，经典类没有这个属性
#新式类继承顺序:F->D->B->E->C->A
#经典类继承顺序:F->D->B->A->E->C
#python3中统一都是新式类
#pyhon2中才分新式类与经典类
