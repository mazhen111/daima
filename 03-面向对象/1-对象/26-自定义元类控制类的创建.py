class mate(type) :
    def __init__(self,class_name,class_bases,class_dic):
        print (class_dic)
        if not class_name.istitle():
            raise TabError("类名首字母必须大写")
        if "__doc__" not in class_dic or not class_dic["__doc__"].strip():
            raise TabError("必须有注释，且注释不能为空")
        super(mate,self).__init__(class_name,class_bases,class_dic)


class Chinses(object,metaclass=mate):
    """
    mazhen
    """
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        print ("mamama%s"%(self.name))
# print (Chinses.__dict__)