"""
继承指的是类与类之间的关系，是一种什么“是”什么的关系，继承的功能之一就是用来解决代码重用问题
继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又可以成为基类或超类，新建的类称为派生类或子类
"""
class Hero:
    def __init__(self, nickname, life_value, aggresivity):
        """

        :param nickname: 账号 
        :param life_value:  生命值
        :param aggresivity:  战斗力
        """
        self.nickname = nickname
        self.life_value = life_value
        self.aggresivity = life_value

    def attack(self, enemy):
        enemy.life_value -= self.aggresivity
        if enemy.life_value <= 0:
            print("%s 已经死了收尸吧" % (enemy.nickname))
class Garen(Hero):
    pass

class Riven(Hero):
    pass
stu1=Garen("HAHAHA",100,30)
print (stu1.__dict__)
