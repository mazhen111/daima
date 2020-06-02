#创建操作
rerson = {"name":"mazhen","age":"20"}
#rerson = dict(name="mazhen",age=20)
import random
rersonlist = {}
for i in range(1,101):
    rersonlist[i] = [random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'],2)]
print (rersonlist)

#增加操作
name = {
    "alex": [23, "CEO", 66000],
    "黑姑娘": [24, "行政", 4000],
}
name["mazhen"] = [26,"rd",3000] #key值相同原来的值会覆盖
print (name.setdefault("maxiaolong",[26,"rd",3000])) #key相同是不会改变，返回原来的key值

#删除操作
#name.pop("mazhen")
#name.popitem() #随意删除一个
#del  name #删除字典
#修改操作
name["黑姑娘"] = [24, "行政", 5000]
print (name.get("mama")) #用get，key值没有别的的时候显示none

name.update(rersonlist) #两个字典合并
print (name)
#查操作
print (name.keys())
print (name.values())
print(name.items())
#循环
info = {
    "name":"小猿圈",
    "mission": "帮一千万极客高效学编程",
    "website": "http://apeland.com"
}
for i in info.keys(): #  # 推荐用这种，效率速度最快
    print (i,info[i])


for i,k in info.items():
    print(i,k)



