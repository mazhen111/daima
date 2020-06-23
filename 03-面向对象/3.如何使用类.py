class LuffyStudent:
    school = "luffycity"
    def learn(self):
        print ("is learn")
    def eat(self):
        print ("is eat")
    def sleep(self):
        print ("is sleep")

#查看类的名称空间
#print (LuffyStudent.__dict__)
print (LuffyStudent.__dict__["sleep"])
print (LuffyStudent.__dict__["eat"])
#查
print(LuffyStudent.sleep) #print (LuffyStudent.__dict__["sleep"])
print (LuffyStudent.eat) #print (LuffyStudent.__dict__["eat"])
#增加
LuffyStudent.county="china"
print (LuffyStudent.__dict__["county"])
#s删除
# del LuffyStudent.school
# print (LuffyStudent.__dict__)
#改
LuffyStudent.school="ZHONGG"
print(LuffyStudent.school)