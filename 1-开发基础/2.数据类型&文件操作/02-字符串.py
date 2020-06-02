#首字母大写
c = "alEX"
print (c.capitalize())
#把字符串变为小写
print (c.casefold())
#把字符串转为大写upper()
print (c.upper())
#字符左右填充  *********************alEX li**********************
print (c.center(50,"*"))
#相同元素的个数
print (c.count("a"))
#先切片在计算相同的元素
print(c.count("a",3))#3为字符串的下标
#判断以什么结尾
print (c.endswith("a"))
#find查找
print (c.find("a" ,1))
#format 字符串数字填充
name = "马振的年龄{0}，身高多少{1}"
print (name.format(20,170))
names=  "马振的年龄{age}，身高多少{height}"
print(names.format(age=24,height=180))
#index查找字符串的下标
print (c.index("l"))
#isdigit 检查字符串是否数字
print (c.isdigit())
#islowe判断字母是否是小写
print (c.islower()) #False
# isspace 判断字符串时候有空格 #
print  (c.isspace())
#isupper判断字符串是否有大写
print (c.isspace())
# join 字符串拼接
c = ['alex','jack','rain']
print ("-".join(c))
str = "this is string exampAAAA....wow!!!  "
#ljust 法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串
print (str.ljust(50,"*"))
#rjust()返回一个原字符串右对齐, 并使用空格填充至长度 width的新字符串
print (str.rjust(50,"*"))
#lower 大写转换成小写
print (str.lower())
#去除字符串的空格
print (str.lstrip())
#replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
print (str.replace("this","mazhen"))
a = str.rsplit(":")
print (a)
#split 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串\
#startswith() 方法用于检查字符串是否是以指定子字符串开头
print (str.startswith("t"))
#strip()方法用于移除字符串头尾指定的字符该方法,只能删除开头或是结尾的字符，不能删除中间部分的字符。
print (str.strip("!!!"))
#swapcase() 方法用于对字符串的大小写字母进行转换。
print (str.swapcase())
#zfill 方法返回指定长度的字符串，原字符串右对齐，前面填充0
print (str.zfill(50))
