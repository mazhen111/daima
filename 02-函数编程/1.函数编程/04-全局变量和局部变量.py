#全局变量
name = "mazhen"
def change():
    # 局部变量强制改全局变量 ,不建议使用，对调试造成误解
    global name
    name = "zhen" #局部变量 在局部变量不可以改全局变量的
    print(locals())
    print (globals())
    print (name)
change()
print (name)