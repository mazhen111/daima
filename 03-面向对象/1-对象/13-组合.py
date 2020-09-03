"""
软件重用的重要方式除了继承之外还有另外一种方式，即：组合
组合指的是，在一个类中以另外一个类的对象作为数据属性，称为类的组合
"""
class  People:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
class Teacher(People):
    def __init__(self,name,sex,age,level,salary):
        super().__init__(name,sex,age)
        self.level=level
        self.salary=salary
    def teach(self):
        print ('%s is teaching' %self.name)
class Student(People):
    def __init__(self,name,sex,age,class_time):
        super().__init__(name,sex,age)
        self.class_time=class_time
    def learn(self):
        print ('%s is learn' %self.name)
stu1=Student("mazhen","男","28","2018:12:12")
# stu1.learn()
"组合"
class Course :
    def __init__(self,course_name,course_price,course_period):
        self.course_name=course_name
        self.course_price=course_price
        self.course_period=course_period
    def tell_info(self):
        print('课程名<%s> 课程价钱<%s> 课程周期<%s>' % (self.course_name, self.course_price, self.course_period))

python=Course('python',3000,'3mons')
teacher1=Teacher("mazhen","man","28","2","100000")
stu1.count=python
stu1.count.tell_info()
teacher1.teach()
stu1.learn()