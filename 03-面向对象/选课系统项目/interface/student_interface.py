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
#选择学校
def add_school_interface(school_name,student_name):
    #判断当前学生用户是否存在学校
    student_obj=models.Student.select(student_name)
    if student_obj.school:
        return False,"当前学生已经选择过学校"
    #22若不存在学校，则给调用的学生对象的方式创建学校
    student_obj.add_school(school_name)
    return  True,"选择学校成功"
#学生选择课程
def get_course_list_interface(student_name):
    #1先获取学生的对象
    student_obj=models.Student.select(student_name)
    student_name=student_obj.school
    if not student_name:
        return False
    #开始获取学校的对象
    school_obj=models.School.select(student_name)
    #3判断当前学校是否也有课程，如没有联系管理员
    course_list=school_obj.course_list
    if not course_list:
        return False,"没有课程请联系管理员"
    return True,course_list
#学生选择学校接口
def add_coure_interface(course_name,student_name):
    #1先判断当前的课程是已经存在学生的列表中
    obj=models.Student.select(student_name)
    #当前学生没有选择学校申请
    if not obj.school:
        return False,"请选择学校"


    if course_name in obj.course_list:
        return False,"学生已经选择过该课程"
    #调用学生接口创建课程
    obj.add_course(course_name)
    return True,"%s选择了%s课程成功"%(student_name,course_name)
#学生分数
def check_sore_interface(student_name):
    obj=models.Student.select(student_name)
    if obj.score:
        print ("1111")
        return  obj.score








