"""
re的匹配语法有以下几种
re.match 从头开始匹配

re.search 匹配包含

re.findall 把所有匹配到的字符放到以列表中的元素返回

re.split 以匹配到的字符当做列表分隔符

re.sub 匹配字符并替换

re.fullmatch 全部匹配

"""



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
# + 匹配前一个字符1次或多次 #['ab', 'ab', 'abb']
print  (re.findall("ab+","ab+cd+ab+babba"))
# ? 匹配前一个字符1次或0次
print(re.search("b?","aaba"))
#'{m}'   匹配前一个字符m次
print (re.search("[0-9]{11}","17912703491").group())
#匹配前一个字符n到m次
print (re.search("[0-9]{3,6}","17812703491"))
# \匹配|左或|右的字符
print (re.findall("abc|ABC","abc12243ABC"))
#(....)分组
print (re.search( "(abc){2}a(123|45)","abcabca456c").group())
#\A 从字符开头匹配
print (re.search("\Aabc","alexabc"))
#\Z 从字符结尾匹配
print(re.search("b$","aaabb"))
#'\d'    匹配数字0-9
print (re.findall("\d","aaa23bb"))
#\D匹配非数字
print(re.findall("\D","aaa23bb"))
#\w 匹配[0-9a-zA-Z]
print (re.search("\w","aaa23bb").group())
#W非匹配[0-9a-zA-Z]
print (re.search("\W","aaa23bb..").group())
#'s'     匹配空白字符
print(re.findall("\s","aaaa\nbbbb\tcccc"))
#'(?P...)' 分组匹配 字典分组
#re.search("(?P[0-9]{4})(?P[0-9]{2})(?P[0-9]{4}")
#re.split 以匹配到的字符当做列表分隔符
print (re.split("[0-9]","aaaa2bbb4ccc"))
#匹配数字
s='9-2*5/3+7/3*99/4*2998+10*568/14'
print (re.split("[\+ \- \* /\]]",s))

""""
re.sub(pattern, repl, string, count=0, flags=0)
用于替换匹配的字符串,比str.replace功能更加强大
"""
print (re.sub('[a-z]+','sb','武配齐是abc123',))


































