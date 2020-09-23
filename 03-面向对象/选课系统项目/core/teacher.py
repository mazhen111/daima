"""
老师视图
"""
from lib import common
from interface import teacher_interface,common_interface

teacher_info={
    "user":None
}
def login():
    while True :
        username=input("请输入账户").strip()
        password=input("请输入密码").strip()
        flag, mag = common_interface.log_interface(
            username,password,user_type="student"
        )
        if flag:
            teacher_info["user"] = username
            print(mag)
            break
        else:
            print(mag)

@common.aute("teacher")
#查看教授课程
def check_course():
    flag,course_list=teacher_interface.check_course_interface(
        teacher_info.get("user")
    )
    if flag:
        print (course_list)
    else:
        print (course_list)
@common.aute("teacher")
#选择交手的课程
def chosse_course():
    #获取学校的名字
    while True:
        flag, school_list = common_interface.get_all_school_interface()
        if not flag:
            print(school_list)
            break
        for index, school_name in enumerate(school_list):
            print("编号%s，学校%s" % (index, school_name))
        choices = input("请输入编号").strip()
        if not choices.isdigit():
            print("请输入数字")
            continue
        choices = int(choices)
        if choices not in range(len(school_list)):
            print("请输入正确的编号")
            continue
        school_name = school_list[choices]
        #2 从选择学校里获取所有课程
        flag2, couse_list = common_interface.get_course_in_school_interface(school_name)
        print (couse_list)
        if not flag2 :
            print (couse_list)
            break
        for index2,couse_list2 in enumerate(couse_list):
            print("编号%s，课程%s" % (index2, couse_list2))
        choices2 = input("请输入编号").strip()
        if not choices2.isdigit():
            print("请输入数字")
            continue
        choices2 = int(choices2)
        if choices2 not in range(len(couse_list)):
            print("请输入正确的编号")
            continue
        #选择课程的名字
        couse_name = couse_list[choices2]
        print (couse_name)


        #调用接口，将课程添加到列表中
        flag3, mag3 = teacher_interface.add_course_interface(
            couse_name,teacher_info.get("user")
        )
        if flag:
            print(mag3)
            break
        else:
            print(mag3)



#查看课程下学生
@common.aute("teacher")
def check_stu_from_course():
    while True:
        #查看教授的课程
        flag, course_list = teacher_interface.check_course_interface(
            teacher_info.get("user")
        )
        if flag:
            print(course_list)
        else:
            print(course_list)
        for index,course_name in enumerate(course_list):
            print("编号%s，课程%s" % (index,course_name))
        choices = input("请输入编号").strip()
        if not choices.isdigit():
            print("请输入数字")
            continue
        choices = int(choices)
        if choices not in range(len(course_list)):
            print("请输入正确的编号")
            continue
        # 选择课程的名字
        course_name=course_list[choices]
        print(course_name)
        print (teacher_info.get("user"))
        flag2, student_list=teacher_interface.get_student_interface(
            course_name,teacher_info.get("user")
        )
        if flag2:
            print (student_list,"222")
            break
        else:
            print (student_list,"11")
            break
@common.aute("teacher")
#修改分数
def change_score_syudent():
    """
     1 先获取老师下的所有的课程，并选择
     2 获取选择老师科恒的学生
     3 调用接口修改学生成绩
    """
    while True:
        # 查看教授的课程
        flag, course_list = teacher_interface.check_course_interface(
            teacher_info.get("user")
        )
        if flag:
            print(course_list)
        else:
            print(course_list)
        for index, course_name in enumerate(course_list):
            print("编号%s，课程%s" % (index, course_name))
        choices = input("请输入编号").strip()
        if not choices.isdigit():
            print("请输入数字")
            continue
        choices = int(choices)
        if choices not in range(len(course_list)):
            print("请输入正确的编号")
            continue
        # 选择课程的名字
        course_name = course_list[choices]
        print(course_name)
        print(teacher_info.get("user"))
        flag2, student_list = teacher_interface.get_student_interface(
            course_name, teacher_info.get("user")
        )
        if not flag2:
            print(student_list)
            break
        for index2,student_name in enumerate(student_list):
            print("编号%s， 学生名%s" % (index2, student_name))
        choices2 = input("请输入编号").strip()
        if not choices2.isdigit():
            print("请输入数字")
            continue
        choices2 = int(choices2)
        if choices2 not in range(len(student_list)):
            print("请输入正确的编号")
            continue
        # 选择课程的名字
        student_name = student_list[choices]
        #修改学生成绩
        score=input("请输入修改的成绩分数：").strip()
        if not score.isdigit():
            print ("输入有误")
            continue
        score=int(score)
        #调用修改学生接口
        flag3,mag = teacher_interface.change_score_interface(
            student_name,score,
            course_name,teacher_info.get("user")
        )
        if flag3:
            print (mag)
            break





func_dict={
    "1":login,
    "2":check_course,
    "3":chosse_course,
    "4":check_stu_from_course,
    "5":change_score_syudent
}
def teacher_view():
    while True:
        print (
            """
        ======================================欢迎来到老师管理界面===============================
         1.登录
         2.查看教授课程
         3.选择教授课程
         4.查看课程下学生
         5.修改学生分数
         ============================================end========================================
            """
        )
        choice = input('请输入功能编号').strip()
        if choice == "q":
            break
        if choice not in func_dict:
            print("输入的序号有误")
            continue
        func_dict.get(choice)()