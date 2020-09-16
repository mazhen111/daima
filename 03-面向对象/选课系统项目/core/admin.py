"""
管理员视图
"""

from lib import common
admin_info={
    "user":None
}
from interface import admin_interface
#注册
def  register():
    while True:
        username=input("请输入用户名").strip()
        password=input("请输入密码").strip()
        re_password=input("请确认密码").strip()
        if password == re_password :
            flag,mag=  admin_interface.admin_register_interface(
                    username,password
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
    pass
#常见讲师
@common.aute("admin")
def create_teacher():
    pass




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



