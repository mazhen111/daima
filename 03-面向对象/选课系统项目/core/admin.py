"""
管理员视图
"""

from lib import common
from interface import common_interface
admin_info={
    "user":None
}
from interface import admin_interface
from interface import  common_interface
#注册
def  register():
    while True:
        username=input("请输入用户名").strip()
        password=input("请输入密码").strip()
        re_password=input("请确认密码").strip()
        if password == re_password :
            flag,mag=  admin_interface.common_interface.log_interface(
                    username,password,user_type="admin"
                )
            if  flag :
                print(mag)
                break

            else:
                print (mag)

        else:
            print ("密码不一致请重新输入")

#登录
def login():
    while True:
        username=input("请输入用户名").strip()
        password=input("请输入密码").strip()
        flag, mag = admin_interface.admin_log_interface(
                    username,password)
        if flag :
            print (mag)
            admin_info["user"]=username
            print (admin_info["user"])
            break
        else:
            print (mag)


#创建学校
@common.aute("admin")
def create_school():
    while True:
        school_name = input("请输入学校名称").strip()
        school_addr = input("请输入学校地址").strip()
        flag, mag = admin_interface.create_school_interface(
            #学校名 学校地址，创建学校的管理员
            school_name, school_addr,admin_info.get("user")
        )

        if flag:
            print(mag)
            break
        else:
            print(mag)

#创建课程
@common.aute("admin")
def create_course():
    while True :
        #1先让管理员选择学校
        #1.1 调用接口选择所有学校的名称打印
        flag,school_list_or_msg=common_interface.get_all_school_interface()
        #2选择学校，在输入课程
        if not  flag :
            print (school_list_or_msg)
            break
        for index,school_name in enumerate(school_list_or_msg):
            print ('编号:%s  学校名：%s'%(index,school_name))
        choices=input("请输入学校编号").strip()
        if not choices.isdigit():
            print("请输入数字")
            continue
        choices=int(choices)
        if choices not in range(len(school_list_or_msg)):
            print ("请输入正确的编号")
        #h获取选择后的学校
        school_name = school_list_or_msg[choices]
        print (school_name,"选择学校")
        #2选择学校后在输入课程
        course_name=input("请输入要创建的课程").strip()
        #3调用创建课程的接口，让管理员创建课程
        print (admin_info.get("user"),"11111")
        flag, mag = admin_interface.create_course_interface(
            # 学校名 学校地址，创建学校的管理员
            school_name, course_name, admin_info.get("user")
        )
        if flag:
            print(mag)
            break
        else:
            print(mag)

    #3调用创建课程接口，让管理员创建课程




#常见讲师
@common.aute("admin")
def create_teacher():
    while True :

        #1让管理员输入创建老师
        teacher_name=input("请输入创建老师的名字").strip()
        #调用老婆接口创建老师
        flag, mag = admin_interface.create_teacher_interface(
            teacher_name, admin_info.get("user")
        )
        if flag:
            print(mag)
            break
        else:
            print(mag)





func_dict={
    "1":register,
    "2":login,
    "3":create_school,
    "4":create_course,
    "5":create_teacher,
}
#管理员函数
def admin_view():
    while True:
        print (
            """
            ===================================欢迎来到管理员界面==========================
                    1.注册
                    2.登录
                    3.创建学校
                    4.创建课程(先选择学校)
                    5.创建讲师
            ============================================end=================================            
            """
        )
        choice = input('请输入功能编号').strip()
        if choice == "q":
            break
        if choice not in func_dict:
            print("输入的序号有误")
            continue
        func_dict.get(choice)()



