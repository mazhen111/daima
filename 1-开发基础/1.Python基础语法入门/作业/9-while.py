# num = 100
# while num >  -2  :
#     if num >=50 :
#         print (num)
#     else:
#         print (49 - num)
#     num -= 1

#使用 while 循环实现输出 1-100 内的所有奇数
# num =1
# while num <= 100:
#     if num %2 != 0 :
#         print (num)
#     num +=1
#
# 使用 while 循环实现输出 1-100 内的所有偶数
# num = 0
# while num <= 100 :
#     if num %2 ==0 :
#         print (num)
#     num +=1
# #使用while循环实现输出2-3+4-5+6…+100 的和
# num = 2
# total = 0
# while num > 100 :
#     if num %2 == 0:
#         total += num
#     else:
#         total -+ num
#     num += 1
# print (num)
# #制作趣味模板程序
# name = input("请输入姓名")
# place = input("请输入地址")
# hobby = input("请输入爱好")
# scm = """敬爱可爱的%s，最喜欢在%s地方干%s"""%(name,place,hobby)
# print (scm)
# year = int(input("请输入年份"))
# if year %4  ==0 and year %100 != 0 :
#     print ("是润年")
# elif year %400 ==0 :
#     print ("是润年")
# else:
#     print ("不是润年")

"""使用while,完成以下图形的输出
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
num =1
while num < 10 :
    if num <=5 :
        print (num * "*")
    else:
        print ((10 - num) *  "*")
    num +=1



