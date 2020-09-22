"""
学生视图


"""
from lib import common
from interface import student_interface,common_interface
student_info={
    "user":None
}
def  register():
    while True:
        username=input("请输入用户名").strip()
        password=input("请输入密码").strip()
        re_password=input("请确认密码").strip()
        if password == re_password :
            flag,mag=  student_interface.student_register_interface(
                    username,password
                )
            if  flag :
                print(mag)
                break

            else:
                print (mag)

        else:
            print ("密码不一致请重新输入")


def login():
    while True :
        username=input("请输入账户").strip()
        password=input("请输入密码").strip()
        flag, mag = common_interface.log_interface(
            username,password,user_type="student"
        )
        if flag:
            student_info["user"] = username
            print(mag)
            break
        else:
            print(mag)




@common.aute("student")
def choice_school():
    #选择学校
    while True:
        flag, school_list = common_interface.get_all_school_interface()
        if not  flag:
            print (school_list)
            break
        for index ,school_name in enumerate(school_list):
            print ("编号%s，学校%s"%(index,school_name))
        choices=input("请输入编号").strip()
        if not choices.isdigit():
            print ("请输入数字")
            continue
        choices=int(choices)
        if choices not in range(len(school_list)):
            print ("请输入正确的编号")
            continue
        school_name=school_list[choices]
        #3开始调用学生学生的接口
        flag,mag = student_interface.add_school_interface(
            school_name,student_info.get("user")
        )
        if flag:
            print(mag)
            break
        else:
            print(mag)

@common.aute("student")
#学生选择课程
def choice_course():
    #1先获取当前学生所在学校的课程
    while True:
        flag,course_list = student_interface.get_course_list_interface(
            student_info.get("user"))
        if not flag:
            print(course_list)
            break
        for index ,choice_name in enumerate(course_list):
            print ("编号%s，学校%s"%(index,choice_name))
        choices=input("请输入编号").strip()
        if not choices.isdigit():
            print ("请输入数字")
            continue
        choices=int(choices)
        if choices not in range(len(course_list)):
            print ("请输入正确的编号")
            continue
        course_name=course_list[choices]
        flag, mag=student_interface.add_coure_interface(
            course_name,student_info.get("user")
        )
        if flag:
            print(mag)
            break
        else:
            print(mag)



@common.aute("student")
#查看分数
def check_sore():
    score=student_interface.check_sore_interface(
        student_info.get("user")
    )
    if not score:
        print ("没有课程")
    print(score)

func_dict={
    "1":register,
    "2":login,
    "3":choice_school,
    "4":choice_course,
    "5":check_sore,
}
def student_view():
    while True:
        print (
            """
          ===========================欢迎来到学生管理系统===============================  
                1.注册
                2.登录功能
                3.选择校区
                4.选择课程（先选择校区，再选择校区中的某一门课程）
                5.查看分数
            ===========================end==============================================
            """
        )
        choice = input('请输入功能编号').strip()
        if choice == "q":
            break
        if choice not in func_dict:
            print("输入的序号有误")
            continue
        func_dict.get(choice)()

