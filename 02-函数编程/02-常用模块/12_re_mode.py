import re
f = open("b.txt","r",encoding="gbk")
data = f.read()

date1 = re.findall("[0-9]{11}",data)
print (date1)
# .匹配除\n任意字符
print (re.match(".","aaaaa1111wsdfveds").group())
# ^ 匹配字符开头的
print(re.match("^a","aaabbbb"))
# $匹配以什么结尾
print (re.search("b$","aaabb"))
# * 匹配*号前的字符0次或多次，从头开始匹配
print (re.search("a*","aaaabac" ))
# + 匹配前一个字符1次或多次



































