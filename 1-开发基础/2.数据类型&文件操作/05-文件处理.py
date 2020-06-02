#创建文件
# f = open(file='./stave.txt',mode="w")
# f.write("Alex  CEO  600\n")
# f.write("mazhen  CEO  600\n")
# f.close()
#只读模式
# f = open(file="./兼职白领学生空姐模特护士联系方式.txt",mode="r" )
# print (f.readline())
# print ("---------------")
# print (f.read())
# f = open(file="./兼职白领学生空姐模特护士联系方式.txt",mode="a")
# f.write("黑姑娘 北京  168  48\n")
# #循环文件
f = open(file="./兼职白领学生空姐模特护士联系方式.txt",mode="r")
for i in f :
    i = i.split()
    height= int(i[2])
    weight = int(i[3])
    if height > 170 and weight <=50 :
        print (i)

