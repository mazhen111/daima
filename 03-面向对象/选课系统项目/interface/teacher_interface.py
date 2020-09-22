"""

老师的接口
"""
from db import models
#查看教授课程
def check_course_interface(teacher_name):
    teacher_obj=models.Teacher.select(teacher_name)
    #让老师对象，调用查教授课程，返回课程
    #course_list=teacher_obj.course_list_from_tea
    course_list=teacher_obj.show_course()
    if not course_list:
        return False,"老师没有选择课程"
    return True,course_list
def add_course_interface(couse_name,teacher_name):
    #获取老师对象
    couse_obj=models.Teacher.select(teacher_name)
    #判断当前课程在老师的课程列表中
    if couse_name in couse_obj.course_list_from_tea:
        return  False,"该课程已存在"
    #那课程加入列表
    couse_obj.add_course(couse_name)


