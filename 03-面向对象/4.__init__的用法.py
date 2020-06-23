class LuffyStudent:
    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age
    school = "luffycity"
    def learn(self):
        print ("is learn")
    def eat(self):
        print ("is eat")
    def sleep(self):
        print ("is sleep")
#后产生对象
stu1 = LuffyStudent("马振","man",18)
print (stu1.__dict__)
#加上__init__方法后，实例化的步骤
# 1、先产生一个空对象stu1
# 2、LuffyStudent.__init__(stu1,'王二丫','女',18)
#查
print(stu1.Name)
print (stu1.Sex)
print (stu1.Age)
#改
stu1.Name = "mazhen"
print (stu1.__dict__)
#增加
stu1.class_name = "python"
print(stu1.__dict__)
#删除
del stu1.Name
print (stu1.__dict__)
print (LuffyStudent.__dict__)