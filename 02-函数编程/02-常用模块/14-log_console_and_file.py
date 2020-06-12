import logging
from  logging import  handlers
#1.生成logger对象
logger = logging.getLogger("web")
logger.setLevel(logging.DEBUG)
class IgnoreBackupLogFilter(logging.Filter):
    """忽略带db backup 的日志"""
    def filter(self, record): #固定写法
        return   "db backup" not in record.getMessage()

#1.1 filer对象添加到logger
#filter 组件
logger.addFilter(IgnoreBackupLogFilter())

#2生成handler对象
cn = logging.StreamHandler()
#fh = logging.FileHandler("web.log")
#按文件大小截取
#fh = handlers.RotatingFileHandler("WEB.log",maxBytes=10,backupCount=3) #maxBytes字节大小 backupCount最大日志数
#按时间截取
fh = handlers.TimedRotatingFileHandler("web.log",when="S",interval=5,backupCount=3) # ,when时间单位 interval时间间隔 最大日志数
# backupCount

#2.把handler对象绑定
logger.addHandler(cn)
logger.addHandler(fh)
#3.生成formatter 对象
#3.1 把formatter 对象 绑定handler对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s')
cn.setFormatter(file_formatter)
fh.setFormatter(console_formatter)

logger.warning("test log ")
logger.info("test log 2")
logger.debug("test log 3")
logger.debug("test log db backup 3")