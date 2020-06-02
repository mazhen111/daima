#BlueBall = input("请输入蓝球")
nun = 0
BlueBallList = []
RedBallList = []
while True :
    if  nun  < 6:
        RedBall = int(input("请输入红球"))
        if RedBall in RedBallList :
            print ("输入数字重复请重新输入")
        elif  RedBall <= 32  :
            RedBallList.append(RedBall)
            nun += 1
        else:
            print ("超出范围")
    else:
        BlueBal= int(input("蓝球"))
        if BlueBal in BlueBallList:
            print("输入数字重复请重新输入")
        elif BlueBal <= 16:
            BlueBallList.append(BlueBal)
            nun += 1
        else:
            print("超出范围")
        if nun > 7 :
            break

print (BlueBallList)
print (RedBallList)





