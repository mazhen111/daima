#函数递归
def num(n):
    n = int(n/2)
    if n >  0 :
        print (n)
        num(n)
num(100)