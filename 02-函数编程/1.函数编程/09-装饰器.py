account = {
    "is_authenticated" :False ,
    "username" : "mazhen" ,
    "password" : "123456"
}
def login (fuct):
    def info(*args,**kwargs):
        if account["is_authenticated"] is False :
            i_username = input("请输入用户名：").strip()
            i_password = input("请输入密码：").strip()
            if i_username == account["username"] and i_password == account["password"]:
                print ("登录成功")
                account["is_authenticated"] = True
                fuct(*args,**kwargs)
            else:
                print ("登录失败")
        else:
            print("用户已登录，验证通过...")
            fuct(*args,**kwargs)
    return info
def home():
    print("---首页----")
@login
def america():
    print("----欧美专区----")
def japan():
    print("----日韩专区----")
@login
def henan(vip_info):
    if vip_info > 3 :
        print("显示更多内容")
    else:
      print("----河南专区----")
home()
america()
henan(4)