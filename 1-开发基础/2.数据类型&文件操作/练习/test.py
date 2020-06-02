__author__ = 'Administrator'
username = input("username:")
#print(username)
name_list = open('name_init','r+')  #'name_init' file created before running
name_text = name_list.readlines()
#print(name_text)

username_i = username+'\n'
if username_i not in name_text :
    print("User doesn't exist,please register.")
    continue_confirm = input("Do you want to register?...Y/N:")
    if continue_confirm == "n" or continue_confirm == "N":
        print("You are leaving.")
    else:
        password1 = input("Input the password:")
        confirm_password = input("Confirm the password:")
        if  password1 == confirm_password :
            name_w = username + '\n'
            name_list.write(name_w)
            name_list.close()

            n_p = username + ':'+password1+'\n'
            name_l_f = open('name_password_init','a+')  #'name_password_init' file created before running
            name_l_f.write(n_p)
            name_l_f.close()

            print("Registration success\n","Welcome user---{name}---login...".format(name=username))
        else:
            print('Incorrect input.')

else:
    locked_f = open("locked_namelist",'r+')
    locked_list = locked_f.readlines()
    if username+'\n' in locked_list :
        locked_f.close()
        print('You are locked,please contact the administrator for unlock')
    else:
        count = 0
        ct_l = 3
        name_l_f = open('name_password_init','r+')  #'name_password_init' file created before running
        namelist_f = name_l_f.readlines()
        while count <ct_l:
            password = input("password:")
            user_info = username+':'+password+'\n'
            if  user_info in namelist_f :
                print("Welcome user---{name}---login...".format(name=username))
                break
            else :
                if count < ct_l-2:
                    print('Incorrect passed,please try again.')

                elif count == ct_l-2 :
                    print('Warning:Only one chance left.')

                count += 1
                if count == ct_l :
                    locked_f.write(username+'\n')
                    locked_f.close()
                    print('The username was locked,please contact the administrator.')

        name_l_f.close()