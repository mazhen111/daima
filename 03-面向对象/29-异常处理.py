#3 异常
#强调一：错误发生的条件如果是可以预知的，此时应该用if判断去预防异常
# AGE=10
# age=input('>>: ').strip()
#
# if age.isdigit():
#     age=int(age)
#     if age > AGE:
#         print('太大了')


#强调二：错误发生的条件如果是不可预知的，此时应该用异常处理机制，try...except
try:
    f=open("2.txt","r",encoding="utf-8")
    print (next(f),end="")
    print(next(f), end="")
    print(next(f), end="")
    print(next(f), end="")
    print(next(f), end="")
    print(next(f), end="")
except StopIteration:
    print("出错啦")