# namelist = ["ma","zhen"]
#追加，数据会追加到尾部
# namelist.append("mazhen")
#插入，可插入任何位置
# namelist.insert(2,"haha")
#合并,可以把另一外列表的值合并进来
# n2 = ["狗蛋","绿毛","鸡头"]
# namelist.extend(n2)
#列表嵌套
# namelist.append(n2)
# print (namelist[-1][0])
#删除操作
#del 直接删除
# del  namelist[-1]
# print (namelist)
#pop 删除会返回删除元素 ，没有对应参数汇报报错，没有添加元素的时候回删除最后一个元素
# print (namelist.pop(1))
#names.remove("eva")
# print (namelist)

#clear 元素清空
# namelist.clear()
# print (namelist)
#查操作
# name = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva']
# #返回从左开始匹配到的第一个eva的索引
# print (name.index("黑姑娘"))
# #返回eva的个数
# print (name.count("黑姑娘"))
#切片
#names[start:end]
#切片的特性是顾头不顾尾，即start的元素会被包含，end-1是实际取出来的值
# names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva']
# print (names[0:2])
# #倒着切
# print (names[-3:])
# # 步长，允许跳着取值 #step 默认是1
# print(names[::2])
# #步长翻转
# print (names[::-1])
# #列表翻转
# names.reverse()
# print (names)
#排序&反转
#a = [83,4,2,4,6,19,33,21]
names = ['金角大王', '黑姑娘', 'rain', 'eva', '狗蛋', '银角大王', 'eva']
# a.sort()
# names.sort()
# print(a)
# print(names)
#列表编译
for i in names :
    print (i)