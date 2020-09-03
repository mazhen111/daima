"""
一封装数据属性，明确的区分内外，控制外部对隐藏的属性的操作行为
"""
class People:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def tell_info(self):
        print ('Name:<%s> Age:<%s>' %(self.__name,self.__age))
    def set(self,name,age):
        if not isinstance(name,str):
            print ("姓名请输入字符串")
            return
        if not isinstance(age,int):
            print ("年龄请输入数字")
            return
        self.__name=name
        self.__age=age
p=People("mazhen",28)
p.tell_info()
p.set("mahaha",30)
p.tell_info()
"""
二封装方法：隔离复杂度
"""
class ATM:
    def __card(self):
        print ("插卡")
    def __auth(self):
        print ("用户认证")
    def __input(self):
        print ("输入取款金额")
    def __print_bull(self):
        print ("打印账单")
    def __take_money(self):
        print ("取款")
    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bull()
        self.__auth()
        self.__take_money()
a=ATM()
a.withdraw()