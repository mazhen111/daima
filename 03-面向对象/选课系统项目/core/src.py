"""
用户试图的主视图
"""
from core import admin
from core import student
from  core import teacher
func_dict={
    "1":admin.admin_view,
    "2":student.student_view,
    "3":teacher.teacher_view
}

def run():
    while True :
        print ("""
        
        ======================欢迎来到选课系统========================
                     1.管理员功能
                     2.学生功能
                     3.老师功能
        ===================end======================================
        """)
        choice=input('请输入功能编号').strip()
        if choice == "q":
            break
        if choice not in func_dict:
            print ("输入的序号有误")
            continue

        func_dict.get(choice)()




