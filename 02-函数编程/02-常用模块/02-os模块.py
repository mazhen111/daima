import os
#得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
print (os.getcwd())
#返回指定目录下的所有文件和目录名:os.listdir()
print (os.listdir())
#os.mkdir("ma")
#函数用来删除一个文件:os.remove()
# os.remove("ma")
#检验给出的路径是否是一个文件：os.path.isfile()
print (os.path.isfile("01-模拟登录.py"))
#检验给出的路径是否是一个目录
print (os.path.isdir("ma"))
#判断是否是绝对路径：os.path.isabs()
print (os.path.isabs("01-模拟登录.py"))
#检验给出的路径是否真地存:os.path.exists()
print (os.path.exists("01-模拟登录.py"))
#返回一个路径的目录名和文件名:os.path.split()
print (os.path.split("01-模拟登录.py"))
#分离扩展名：os.path.splitext()
print (os.path.dirname('01-模拟登录.py'))
#获取路径名：os.path.dirname()
print (os.path.dirname(__file__))
#获得绝对路径: os.path.abspath()
print (os.path.abspath(__file__))
#获取文件名：os.path.basename()
print (os.path.basename(__file__))
print (os.getenv("HOME"))
print (os.environ)
#设置系统环境变量，仅程序运行时有效：os.environ.setdefault('HOME','/home/alex')
os.environ.setdefault("ma","/home/ma")
print (os.environ)
print (os.name)
# os.rename("zhen","mazhen123456")
#os.makedirs("zhen/ma/zhen/12/zhen")
# os.removedirs("zhen")
print (os.stat_result("02-os模块.py"))
#print (os.get_terminal_size())






