"""
练习2：模仿王者荣耀定义两个英雄类， (10分钟)
要求：
英雄需要有昵称、攻击力、生命值等属性；
实例化出两个英雄对象；
英雄之间可以互殴，被殴打的一方掉血，血量小于0则判定为死亡。
"""
class Garen:
    camp="Demacia"
    def __init__(self,nickname,life_value,aggresivity):
        """
        
        :param nickname: 账号 
        :param life_value:  生命值
        :param aggresivity:  战斗力
        """
        self.nickname=nickname
        self.life_value=life_value
        self.aggresivity=life_value
    def attack(self,enemy):
        enemy.life_value-=self.aggresivity
        if enemy.life_value <= 0 :
            print ("%s 已经死了收尸吧"%(enemy.nickname))


class Riven :
    camp = "Demacia"

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
g1=Garen('草丛伦',100,30)
r1=Riven('可爱的锐雯雯',80,50)
print (r1.life_value)
g1.attack(r1)
print (r1.life_value)

