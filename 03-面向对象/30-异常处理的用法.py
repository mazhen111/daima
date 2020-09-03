#多分支被监测的代码块抛出的异常有多种可能性，并且我们需要针对每一种异常类型都定制专门的处理逻辑
try:
    print('===>1')
    #name
    print('===>2')
    l=[1,2,3]
    # l[100]
    print('===>3')
    d={}
    #d['name']
    print('===>4')
# except NameError as e:
#     print('--->',e)
#
# except IndexError as e:
#     print('--->',e)
#
# except KeyError as e:
#     print('--->',e)
#
#
# print('====>afer code')
#万能异常：Exception,被监测的代码块抛出的异常有多种可能性，
# 并且我们针对所有的异常类型都只用一种处理逻辑就可以了，那就使用Exception
# except Exception as f:
#     print ("异常报错%s"%(f))
#其他结构
except Exception as f:
    print ("异常报错%s"%(f))
else :
    print('在被检测的代码块没有发生异常时执行')
finally:
    print ("清理日志")

#自动触发异常 raise

class peole:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        if not isinstance(self.name,str):
            raise  TypeError('名字必须传入str类型')
        if not  isinstance(self.age,int):
            raise TypeError('名字必须传入int类型')
            range
    def run(self):
        pass


a=peole("mazhen",20)
class MyException(BaseException):
    def __init__(self,msg):
        super(MyException,self).__init__()
        self.msg=msg
    def __str__(self):
        return '<%s>' % self.msg
raise MyException("报错了检查源码")