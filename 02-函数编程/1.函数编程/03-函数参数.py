#默认参数
# def reister(name,age,major,country="US"):
#     """
#     学籍注册程序
#     :param name:
#     :param age:
#     :param major:
#     :param country:
#     :return:
#     """
#     info = """
#     name : %s
#     age: %s
#     major: %s
#     country : %s
#     """%(name,age,major,country)
#     print (info)
# reister("张三",22,"CS")
# #关键参数
#  #优先级 位置参数> 关键参数
# reister(name="mazhen",age=22 ,major="Cs")
#非固定参数
def stu_register(name,*args,**kwargs):
    print (name,args,kwargs)
    print (kwargs.get("province"),args[0])

stu_register("mazhen",22,province="ShanDong")

#args 存的是元组 kwargs存的是字典
