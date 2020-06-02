names=["金角大王", "黑姑娘", "rain", "eva", "狗蛋", "银角大王", "eva","鸡头"]
#1.通过names.index()的方法返回第2个eva的索引值
# for i,x in enumerate(names):
#     if x == "eva":
#         print (i)
#2把以上的列表通过切片的形式实现反转
# print (names[::-1])
#3 打印列表中所有下标为奇数的值
# for i ,x in enumerate(names):
#     if i %2 == 1 :
#         print ( i,x)
#通过names.index()方法找到第2个eva值 ，并将其改成EVAd
for i in names :
    # print (names.index(i))
    print(i)
    if i == "eva" :
        names[6] = "EVA"
print (names)
