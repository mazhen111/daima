"""
    对象1：王二丫
        特征：
            学校='luffycity'
            名字='王二丫'
            性别='女'
            年龄=18
        技能：
            学习
            吃饭
            睡觉

    对象2：李三炮
        特征：
            学校='luffycity'
            名字='李三炮'
            性别='男'
            年龄=38
        技能：
            学习
            吃饭
            睡觉

    对象3：张铁蛋
        特征：
            学校='luffycity'
            名字='张铁蛋'
            性别='男'
            年龄=48
        技能：
            学习
            吃饭
            睡觉

    总结现实中路飞学院的学生类：
        相似的特征
            学校='luffycity'

        相似的技能
            学习
            吃饭
            睡觉


"""

class LuffyStudent:
    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age
    school = "luffycity"
    def learn(self,x):
        print ("%s is learn %s"%(self.Name,x))
    def eat(self):
        print ("%sis eat"%(self.Name))
    def sleep(self):
        print ("%s is sleep"%(self.Name))
stu1=LuffyStudent('王二丫','女',18)
stu2=LuffyStudent("李三炮","男",38)
print (stu1.__dict__)
print (stu2.__dict__)
# 对象：特征与技能的结合体
#类：类是是一系列对象相似的特征与相似的技能的结合体
#类中的数据属性：是所以对象公用的
print (stu1.school,id(stu1.school))
print (stu2.school,id(stu2.school))
#类的函数属性：是绑定给对象使用的，绑定到不同的对象是不同的绑定方法，对象调用绑定方法时，会把对象本身当做第一个传入，传给self
stu1.learn(112)
stu2.eat()