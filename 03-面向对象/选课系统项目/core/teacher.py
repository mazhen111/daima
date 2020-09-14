"""
老师视图
"""
from lib import common
teacher_info={
    "user":None
}
def login():
    pass
@common.aute("teacher")
def check_course():
    pass
@common.aute("teacher")
def chosse_course():
    pass
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