import datetime
#返回当前的datetime日期类型
d=datetime.datetime.now()
print (d.year,d.month,d.timestamp(),d.timetuple())
#把一个时间戳转为datetime日期类型
print (datetime.date.fromordinal(3222222))
#2时间运算
print (datetime.datetime.now() + datetime.timedelta(-15))