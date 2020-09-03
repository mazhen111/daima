"""

在子类中，新建的重名的函数属性，在编辑函数内功能的时候，
有可能需要重用父类中重名的那个函数功能，应该是用调用普通函数的方式，即：类名.func()，此时就与调用普通函数无异了，因此即便是self参数也要为其传值
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
    camp="demaxiya"

class Riven(Hero):
    camp="Noxus"
stu1=Garen("mazhen",100,20)
stu2=Riven("sundan",100,80)
stu2.attack(stu1)
print (stu1.camp)