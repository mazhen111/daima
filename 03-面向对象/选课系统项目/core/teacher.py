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
        couse_name = couse_list[choices]
        print (couse_name)


        #调用接口，将课程添加到列表中
        teacher_interface.add_course_interface(
            couse_name,teacher_info.get("user")
        )
        return True, "{%s}课程创建成功" % {couse_name}




@common.aute("teacher")
def check_stu_from_course():
    pass
@common.aute("teacher")
def change_score_syudent():
    pass

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