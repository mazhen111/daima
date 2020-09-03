"""
练习1：编写一个学生类，产生一堆学生对象， (5分钟)
要求：
有一个计数器（属性），统计总共实例了多少个对象
"""
class Student:
    count =0
    school="清华"
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        Student.count+=1
    def learn(self):
        print ('%s is learing' %self.name)
stu1=Student("mazhen","male","40")
stu2=Student("maxiaolong","male","30")
stu1.learn()
print (Student.count)
