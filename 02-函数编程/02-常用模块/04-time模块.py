import time
#返回当前时间的时间戳。
print (time.time())
#将一个时间戳转换为当前时区的struct_time。若secs参数未提供，则以当前时间为准
a = time.localtime()
#gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time
print (time.gmtime())
#返回当前时间的时间戳
print (time.mktime(a))
#延时
# time.sleep(10)
b = (time.strftime("%Y-%m-%d-%X",time.localtime()))
# time.strftime(b ,"%Y-%m-%d-%X")
print (b)

c = time.mktime(time.strptime("2020-05-12-19:00:18","%Y-%m-%d-%X"))
print (c)