"""
property是一种特殊的属性，访问它时会执行一段功能（函数）然后返回值

例一：BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）

成人的BMI数值：

过轻：低于18.5

正常：18.5-23.9

过重：24-27

肥胖：28-32

非常肥胖, 高于32

体质指数（BMI）=体重（kg）÷身高^2（m）

EX：70kg÷（1.75×1.75）=22.86

"""

# class   People:
#     def __init__(self,name,waight,height):
#         self.name=name
#         self.waight=waight
#         self.height=height
#     @property
#     def amb(self):
#         return  self.waight / (self.height ** 2)
# a= People("name",85,1.72)
# print (a.amb)
#a.amb 不不能赋值
class people:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        print ("name")
        return  self.__name
    @name.setter
    def name(self,var):
        if not isinstance(var,str):
            print ("名字请输入字符串")
            return
        self.__name=var
    @name.deleter
    def name(self):
        print ("不能删除")

a=people("ma")
print (a.name)
a.name="mazhen"
print (a.name)
del a.name