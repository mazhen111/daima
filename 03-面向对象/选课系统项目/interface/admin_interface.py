"""
管理员接口
"""
from db import models
def admin_register_interface(user,password):


      #1.判断用户是否存在
      #1.1 若存在不允许注册 ，返回用户给视图
      obj=models.Admin.select(user)
      if obj:
            return False ,"账户已存在"
      else:
            #1.2 若不存在则注册
            admin_obj=models.Admin(user,password)
            #对象调用save（）将把admin_obj传给save方法
            admin_obj.save()
            return True,"注册成功"


def admin_log_interface(user,password):
    admin_obj = models.Admin.select(user)
    if not admin_obj :
        return False,"用户不存在"
    if  password == admin_obj.pwd:
        return True,"登录成功"
    else:
        return False ,"登录失败"
#创建学校的接口
def create_school_interface(school_name,school_addr,user):
    """
    :param school_name: 
    :param school_addr: 
    :return:
     1 查看当前学校是否存在
     2若学校存在返回False告诉用户学校存在
     3 学校不存在，择创建学校 有管理远创建
     
    """
    print(user)
    school_obj=models.School.select(school_name)
    if school_obj:
        return False ,"学校已存在"
   #3 学校不存在，择创建学校 有管理远创建
    admin_obj = models.Admin.select(user)
    admin_obj.create_school(
        school_name, school_addr
    )
    #4返回创建学校成功给视图
    return  True,'f[{school_name}]'











    pass



