#创建集合 集合有去重的功能
a = {1,2,3,4,2,'alex',3,'rain','alex'}
b = [7, 8, 9, 4, 'mazhen', 'rain']
print (a)
#帮列表去重
namelist = [1, 2, 3, 4, 2, 'alex', 3, 'rain', 'alex']
print (list(set(namelist)))
#集合增删查 集合不可改
a.add("mazhen")
a.add("zhenma")
print (a)
#删除
a.discard("mazhen")
print(a)
#删除pop 随机删除少用
a.pop()
print (a)
#两集合合并
a.update(b)
print (a)

s_1024 = {"佩奇","老男孩","海峰","马JJ","老村长","黑姑娘","Alex"}
s_pornhub = {"Alex","Egon","Rain","马JJ","Nick","Jack"}
#交集
print(s_1024 & s_pornhub)
#{'Alex', '马JJ'}
#并集
print(s_1024 | s_pornhub)
#'Alex', 'Egon', '黑姑娘', 'Jack', '老男孩', '马JJ', '佩奇', 'Rain', 'Nick', '海峰', '老村长'}
#差集
print (s_1024 - s_pornhub)
#{'老村长', '佩奇', '老男孩', '黑姑娘', '海峰'}
print (s_pornhub - s_1024)
#{'Nick', 'Rain', 'Egon', 'Jack'}
#对称差集  对称差集, 把脚踩2只船的人T出去
print (s_1024 ^ s_pornhub)
#两个集合之间一般有三种关系，相交、包含、不相交。在Python中分别用下面的方法判断：
# 判断2个集合是不是不相交，返回True or False
print (s_1024.isdisjoint(s_pornhub))
#判断s_1024是不是s_pornhub的子集，返回True or False
print (s_1024.issubset(s_pornhub))
# 判断s_1024是不是s_pornhub的父集，返回True or False
print (s_1024.issuperset(s_pornhub))





