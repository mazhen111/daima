"""
学生视图


"""
from lib import common
student_info={
    "user":None
}
def  register():
    pass

def login():
    pass
@common.aute("student")
def choice_school():
    pass
@common.aute("student")
def choice_course():
    pass
@common.aute("student")
def check_sore():
    pass

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

