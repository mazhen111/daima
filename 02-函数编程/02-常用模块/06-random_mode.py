import random
import string
print (random.randrange(1,10)) #返回1-10之间的随机数,不包过10
print (random.randint(1,10))#返回1-10之间的随机数 包括10
print (random.randrange(0,100,2))#返回随机数的偶数
print (random.random())#返回一个小数随机数
print(random.choice("abce3#$@1")) #返回一个给定数据集合中的随机字符
print (random.sample("abcdefghij0",3))
#生成随机数字符串
print ("".join(random.sample(string.ascii_lowercase+ string.digits,6)))
a = list(range(100))
random.shuffle(a)
print (a)
