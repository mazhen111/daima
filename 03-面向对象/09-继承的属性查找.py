class Foo :
    def f1(self):
        print ("Foo.f1")
    def f2(self):
        print('Foo.f2')
        self.f1() #b.f1()
class Bar(Foo) :
    def f1(self):
        print("Bar.f1")
b=Bar()
print (b.__dict__)
b.f1()
b.f2()
"""
查找规则 再去对象查找，再去类查找，再去父类查找
"""
"""
Bar.f1
Foo.f2
Bar.f1
"""