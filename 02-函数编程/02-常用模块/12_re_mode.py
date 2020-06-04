import re
f = open("b.txt","r",encoding="gbk")
data = f.read()

date1 = re.findall("[0-9]{11}",data)
print (date1)