name = input("输入你的姓名:")
age = int(input("输入你的年龄:"))
height = input("输入你的身高:")
question = input("你是不是全身都黑:")
msg = '''
-------------Personal Info-----------
Nane      : %s
Age       : %d
Height    : %s
Question  : %s
''' % (name,age,height,question)
print (msg)
if question == "y" or question== "Q":
    print ("我不信，让我看看。。。")

