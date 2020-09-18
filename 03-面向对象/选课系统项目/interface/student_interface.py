from db import models
def student_register_interface(user,password):
    #判断用户是否存在
    #1.1用户不存在时创建用户
    obj=models.Student.select(user)
    if obj:
        return  False ,"学生用户存在"
    #1.2用户不存在创建用户
    else:
        student_obj=models.Student(user,password)
        student_obj.save()
        return  True,"%s创建成功"%{user}
def add_school_interface(school_name,student_name):
    pass




