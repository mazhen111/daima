"""
公告方法


"""

def aute(role):
    """
    
    :param rele: 角色  
    :return: 
    """
    from core import admin,student,teacher

    def login_auth(func):
         def inner(*args,**kwargs):
             if role == "admin":
                 if admin.admin_info["user"]:
                    res=func(*args,**kwargs)
                    return  res
                 else:
                     admin.login()
             if role == "student":
                 if student.student_info["user"]:
                     res = func(*args, **kwargs)
                     return res
                 else:
                     student.login()
             if role == "teacher":
                 if teacher.teacher_info["user"]:
                    res=func(*args,**kwargs)
                    return  res
                 else:
                     teacher.login()

             else:
                 print("当前视图没有权限")
         return inner
    return login_auth


