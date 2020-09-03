"""
'''
面向过程：核心是过程二字，过程指的是解决问题的步骤，设计一条流水线，机械式的思维方式
优点：复杂的问题流程化，进而简单化
缺点：可扩展性差
'''
"""
import  json
def interactive():
    username = input("请输入用户").strip()
    passwd = input("请输入密码").strip()
    return {

        "user":username,
        "password": passwd
    }

def check(user_info):
    is_valid = True
    if len(user_info["user"]) == 0:
        print ("用户名不能为空")
        is_valid = False
    if  len(user_info["password"]) < 6 :
        print ("密码格式不正确")
        is_valid = False
    return {
        "user_info":user_info,
         "is_valid":is_valid
    }

def register(user_info):
    if user_info["is_valid"]:
        with open("test.json","a",encoding="utf-8") as f :
            json.dump(user_info["user_info"],f)

def main():
    user_info = interactive()
    check_info=check(user_info)
    register(check_info)


if __name__ == '__main__':
    main()