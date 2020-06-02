Name_File = "mazhen"
print (Name_File)
Age = float(3.11)
print (Age)
print (type (Age))
print ( type (Name_File))
#字符串
"""多引号的作用"""
msg ="""
今天我想写首小诗，
歌颂我的同桌，
你看他那乌黑的短发，
好像一只炸毛鸡。
"""
print (msg)
#字符串拼接
name = "Alex Li"
age = "22"
print ((name+age)*10)
names = ["Alex","Jack","Rain","Rachel","Mack"]
#输出列表所有的元素
for i in range(len(names)) :
    print(names[i])

#取出"Rain
print(names[1])
#插入在Rain后面插入小明
names.insert(3,"小明")
print(names)
#追加
names.append("mazhen")
print(names)
#修改
names[1] = "jiushi"
print (names)
#删除
# names.remove(2)
# print (names)
#命令嵌套
del names[names.index("Rain")]
print (names)

