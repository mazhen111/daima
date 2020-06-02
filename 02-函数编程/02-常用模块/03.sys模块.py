import  sys
#命令行参数List，第一个元素是程序本身路径
# print (sys.argv[1])
#获取Python解释程序的版本信息
print (sys.version)
#返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print (sys.path)
#返回操作系统平台名称
print (sys.platform)
#获取最大递归层数
print (sys.getrecursionlimit())
#获取解释器默认编码
print (sys.getdefaultencoding())
#获取内存数据存到文件里的默认编码
print (sys.getfilesystemencoding)