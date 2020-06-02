import  os
f = open("date.txt","r+")
accounts_list = f.readline().strip().split(",")
rae_data = f.readlines()
accounts = {}
for i in  rae_data :
    i = i.strip()
    if not i.startswith("#"):
        items = i.split(",")
        print (items)
        accounts[items[0]] = items
f.close()

print ("qq",accounts_list)
menu = """
打印个人信息
修改个人信息
修改密码
"""

#打印个人信息
def print_personal_info (account_dic,username):
    """
    打印个人函数
    :param account_dic: 传入的字典 
    :param username:  查询的用户名
    :return: 
    """
    account_info = account_dic.get(username)
    print (account_info[1],"11111")
    Name = account_info[0]
    Age = account_info[2]
    Job = account_info[4]
    Phone = account_info[5]
    Dept = account_info[3]
    info  = '''
    ------------------
    Name  : %s  #代表 name 
    Age   : %s
    Job   : %s
    Phone : %s
    Dept  : %s
    ------------------
    ''' %(Name,Age,Job,Phone,Dept)
    print (info)
#修改个人信息
def save_back_to_file(account_dic,username,account_list,modify,Modify_classification):
    """
    #修改个人信息
    :param account_dic: 个人信息字典
    :param username: 修改的用户
    :param account_list:  个人信息的列表
    :param modify:  修改的内容
    :param Modify_classification: 修改的分类 
    :return: 
    """
    print ("mazhen11111")
    account_info = account_dic.get(username)
    Modify_index = accounts_list.index(Modify_classification)
    account_info[Modify_index] = modify
    print (account_info)
    f = open("win_data.txt","w",encoding="GBK")
    for i  in account_dic.values():
        if  username in i :
            a= ",".join(account_info)+ '\n'
        else:
            a = ",".join(i) + '\n'

        f.write(a)
    f.close()
    os.replace('win_data.txt','date.txt')

num = 0
while  num < 3 :
    name = input("请输入账号").strip()
    password  =  input("请输入密码").strip()
    if name in accounts.keys() and password == accounts.get(name)[1] :
        print ("登录成功")
        print("-------------------welcome alex --------------------")
        for i,a in enumerate(menu.split()):
            print (i+1,a)
        while True :
            SerialNumber = input("请输入序号").strip()
            print (SerialNumber)
            print (len(menu.split()))
            if SerialNumber.isdigit() and len(menu.split()) >= int(SerialNumber)    :
                if SerialNumber == "1" :
                    username = input("请输入查询的用户名称").strip()
                    print_personal_info(accounts,username)
                elif SerialNumber == "2" :
                    Modifyusername = input("请输入修改的用户名称").strip()
                    Modify_class = input("请输入修改的分类")
                    modify_in = input("请输入修改的内容")
                    save_back_to_file(accounts,Modifyusername,accounts_list,modify_in,Modify_class)
                    print ("第二个功能")
                elif SerialNumber == "3":
                    print("第三个功能")

            elif SerialNumber == "q":
                exit()
            else:
                print ("输入非法字符请重试")
    else:
        print ("登录失败")
        num +=1










