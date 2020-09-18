"""
管理员接口
"""
from db import models
from interface import common_interface
# def admin_register_interface(user,password):
#
#
#       #1.判断用户是否存在
#       #1.1 若存在不允许注册 ，返回用户给视图
#       common_interface.log_interface(user,password,"admin")


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


def create_course_interface(school_name,course_name,admin_name):
    #1查看对象是否存在
    #先获取学校的列表
    school_obj=models.School.select(school_name)
    if course_name in school_obj.course_list:
        return False,"当前课程已存在"
    #1.2若课程不存在，则创建课程
    print (admin_name,"admin_name")
    admin_obj=models.Admin.select(admin_name)
    admin_obj.create_course(
        school_obj,course_name)
    #print (school_obj,course_name)
    #return True ,course_name,"绑定成功绑定给",school_name,"校区"
    return True,"11111"
#创建老师接口

def create_teacher_interface(teacher_name, admin_name,teacher_pass="123"):
    teacher_obj=models.Teacher.select(teacher_name)
    if teacher_obj :
        return False,"老师已存在"
    #2
 #1.2若课程不存在，则创建课程
    admin_obj=models.Admin.select(admin_name)
    admin_obj.create_teacher(
        teacher_name,teacher_pass
    )
    return True,"{%s}老师创建成功"%{teacher_name}


















