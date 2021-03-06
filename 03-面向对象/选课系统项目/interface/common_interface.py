#获取所有学校的接口
from conf import settings
from db import models
import os
#获取学校文件路径
def get_all_school_interface():
    school_dir=os.path.join(
        settings.DB_PATH, "School"
    )
    #判断学校是否存在
    if not os.path.exists(school_dir):

        return False,"没有学校，请联系管理员"
    #若文件存在，则获取问价中所有文件的名字
    school_list=os.listdir(school_dir)
    return  True,school_list
#登录公告接口
def log_interface(user,password,user_type):
    if user_type == "admin":
        obj = models.Admin.select(user)
    elif user_type == "student":
        obj = models.Student.select(user)
    elif user_type == "teacher":
        obj = models.Teacher.select(user)
    else: False,"登录用户角色不存在"

    #判断用户存在
    if  obj :
        if password == obj.pwd:
            return True, "登录成功"
        else:
            return False, "登录失败"

    else:
        return False,"用户不存在"
#获取学校的所有课程
def get_course_in_school_interface(school_name):
    #获取学校对象
    school_obj=models.School.select(school_name)
    #获取课程列表
    course_list=school_obj.course_list
    if not course_list:
        return False,"该学校没有课程"
    return True,course_list
