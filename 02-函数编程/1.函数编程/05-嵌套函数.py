#嵌套函数
# name = "小圆圈"
# def change():
#     name = "小猿圈，自学编程"
#     def change1():
#         name = "小猿圈，自学编程不要钱"
#         print ("第三层",name)
#     change1()
#     print ("第二层",name)
# change()
# print ("第一层",name)
#匿名函数
#匿名函数就是不需要显式的指定函数名
def calc(x):
    return x ** 2
print (calc(3))
#匿名函数
#map() 会根据提供的函数对指定序列做映射
calc = map(lambda x : x ** 2,[1,2,4,8])
for i in calc :
    print (i)


