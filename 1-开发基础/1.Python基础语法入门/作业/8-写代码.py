num = 0
while num <= 3 :
    name = input("请输入姓名")
    password = input("请输入密码")
    if name == "seven" and password == "123" :
        print ("登录成功")
        break
    else:
        print ("登录失败")
    num += 1
