import logging
#logging.warning("user [alex] attempted wrong password more than 3 times")
# logging.critical("server is down")
# logging.error("server is down")
#想把日志写到文件里
#logging.basicConfig(filename="1.log",level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
#自定义日志格式

"""
%(levelno)s   数字形式的日志级别
%(levelname)s  文本形式的日志级别
%(pathname)s    调用日志输出函数的模块的完整路径名，可能没有
%(filename)s     调用日志输出函数的模块的文件名
%(module)s       调用日志输出函数的模块名
%(funcName)s	   调用日志输出函数的函数名
%(lineno)d        调用日志输出函数的语句所在的代码行
%(created)f     当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d   输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s    字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d     线程ID。可能没有
%(threadName)s     线程名。可能没有
%(process)d        进程ID。可能没有
%(message)s     用户输出的消息

"""
logging.basicConfig(
    filename="log_test.log",level=logging.DEBUG,
    format='%(asctime)s %(message)s-%(levelno)s-%(levelname)s-%(filename)s-%(funcName)s' ,
    datefmt="%Y-%d-%m %I:%M:%S %p",
)
def sayhi():
    logging.info("ma when this event was logged.")
sayhi()
logging.warning('is when this event was logged.')
logging.error("server is down")
