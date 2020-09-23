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
#老师添加课程接口
def add_course_interface(couse_name,teacher_name):
    #获取老师对象
    couse_obj=models.Teacher.select(teacher_name)
    #判断当前课程在老师的课程列表
    if couse_name in couse_obj.course_list_from_tea:
        return  False,"该课程已存在"
    #那课程加入列表
    couse_obj.add_course(couse_name)
    return True, "选择学校成功"
#老师获取课程学生接口
def get_student_interface(course_name,teacher_name):
    teacher_obj=models.Teacher.select(teacher_name)
    student_list=teacher_obj.get_student(course_name)
    #判断课程是否有课程
    if not student_list:
        return False,"没有课程没有选择学生"
    return True, student_list
def change_score_interface(student_name,score,course_name,teacher_name):
    #获取老师对象
    teacher_obj=models.Teacher.select(teacher_name)
    #2让老师对象调用修改分数的方法
    teacher_obj.change_score(student_name,score,course_name)
    return  True,"分数修改成功"


