import shutil
#将文件内容拷贝到另一个文件里，文件必须存在
#shutil.copyfileobj(open("1.txt","r"),open("2.txt","w"))
#拷贝文件文件 目标文件无需存在
#shutil.copyfile("1.txt","3.txt")
#仅拷贝权限。内容、组、用户均不变
#shutil.copymode("1.txt","4.txt")
#拷贝文件权限
#shutil.copy("1.txt","b.txt")
#拷贝文件和状态信息
#shutil.copy2("1.txt","c.txt")
#递归的去拷贝文件夹 去除*.pyc', 'tmp*
#shutil.copytree("../1.函数编程","02-常用模块",ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
#递归的去删除文件
#shutil.rmtree("c.txt")
#递归的去移动文件，它类似mv命令，其实就是重命名。
#shutil.move('folder1', 'folder3')
#打包
ret = shutil.make_archive("data_bak","zip",root_dir="../02-常用模块")
