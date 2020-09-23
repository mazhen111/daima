"""
用于存放
学校类，学员类，课程类 讲师类，管理员类
"""
from db import db_handler

class Base:

    def save(self): #保存数据 》注册》保存>更新数据
        db_handler.svae_data(self)
    @classmethod
    def select(cls,username):#的用户登录
        obj = db_handler.select_data(cls,username)
        return obj

class Admin(Base):
    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd

    #创建学校
    def create_school(self,school_name,school_addr):
        school_obj=School(school_name,school_addr)
        school_obj.save()

    #创建课程
    def create_course(self,school_obj,course_name):
        course_obj=Course(course_name)
        course_obj.save()
        #获取当前学校对象，并把课程添加课程列表
        school_obj.course_list.append(course_name)
        print (school_obj.course_list)
        #更新学校
        print("更新学校")
        school_obj.save()



    def create_teacher(self,teacher_name,teacher_pass):

        teacher_obj=Teacher(teacher_name,teacher_pass)
        teacher_obj.save()



class School(Base):
    def __init__(self, name,addr):
        self.user = name
        self.addr = addr
        #课程对象空列表
        self.course_list=[]


class Student(Base):
    def __init__(self,student_name,student_pwd):
        self.user=student_name
        self.pwd=student_pwd
        #一个学生只能有校区小区
        self.school = None
        #一个学生可以选择多个课程
        self.course_list=[]
        self.score={} #{"course_name:0}
    #添加学校的方法
    def add_school(self,school_name):
        self.school=school_name
        self.save()
    # 学生添加课程的方法
    def add_course(self,course_name):
        #1 学生课程列表添加课程
        self.course_list.append(course_name)
        #2给学生默认分数
        self.score[course_name]=0
        print (self.score)
        self.save()
        #3学生选择课程，添加学生
        obj=Course(course_name)
        obj.student_list.append(
            self.user
        )
        obj.save()


class Course(Base):
    def __init__(self,course_name):
        self.user = course_name
        self.student_list=[]

class Teacher(Base):
    def __init__(self,teacher_name,teacher_pwd):
        self.user=teacher_name
        self.pwd=teacher_pwd
        self.course_list_from_tea=[]
    def show_course(self):
        print("222")
        return  self.course_list_from_tea


    def add_course(self,couse_name):
        self.course_list_from_tea.append(couse_name)
        self.save()
    def get_student(self,course_name):
        course_obj=Course.select(course_name)
        return  course_obj.student_list
    #老师修改分数方法
    def change_score(self,student_name,score,course_name):
        student_obj=Student.select(student_name)
        student_obj.score[course_name]=score
        print (student_obj.score)
        student_obj.save()



