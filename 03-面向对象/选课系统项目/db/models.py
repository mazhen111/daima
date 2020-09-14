"""
用于存放
学校类，学员类，课程类 讲师类，管理员类
"""
from db import db_handler
class Admin:
    def __init__(self,user,pwd):
        self.user=user
        self.pwd=pwd
    def save(self):
        db_handler.svae_data(self)
    @classmethod
    def select(cls,username):
        obj = db_handler.select_data(cls,username)
        return obj
class School:
    pass
class Student:
    pass

class Course:
    pass

class Teacher:
    pass