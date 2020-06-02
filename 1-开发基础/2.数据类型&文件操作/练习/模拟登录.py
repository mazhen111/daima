username = input("请输入用户:")
name_list = open("name_init","r+")
name_text = name_list.readlines()
uaername_i = username +"\n"
if uaername_i  not in name_text :
    print (uaername_i ,name_text)
    print ("User doesn't exist,please register.")
    continue_confirm = input("Do you want to register?...Y/N:")
    if continue_confirm == "Y" or  continue_confirm == "y" :
        password1 = input("请输入密码")
        confirm_password = input("请再次输入密码")
        if password1  == confirm_password :
            name_w = username+'\n'
            name_list.write(name_w )
            name_list.close()
            n_p = username + ":"+ password1+'\n'
            name_f = open("name_password_init" ,"a+")
            name_f.write(n_p)
            name_f.close()
        else:
            print ("密码不一致")
    else:
        print ("You are leaving.")
else:
    locked_f = open("locked_namelist" ,"r+")
    locked_line =locked_f.readlines()
    if username + "\n" in locked_line :
        print ("账户已经锁定")
    else:
        count = 0
        ct_1 = 3
        name_1_f = open("name_password_init","r+")
        name_list_1 = name_1_f.readlines()
        while count < ct_1 :
            password = input("请输入密码：")
            user_info = username +  ":" + password +'\n'
            if user_info in name_list_1 :
                print("登录成功")
                break
            count += 1
            if count == 3 :
                locked_f.write(username+'\n')
                locked_f.close()
                print ("账户已锁定，请联系管理员")
















