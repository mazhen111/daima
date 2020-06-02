import random
game = 0
while  game < 3:
    number = random.randint(0,100)
    num = int(input("请输入数字"))
    if num >  number :
        print ("猜大了")
    elif num <  number :
        print ("猜小了")
    else:
        print ("猜对了")
        break #终止循环
    game += 1
    if game == 3:
        option = input("继续请输入y或Y，N或N退出")
        if option ==  "y"  or option == "Y" :
            game = 0
        elif option ==  "n"  or option == "N" :
            break
