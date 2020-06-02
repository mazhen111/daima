#高阶函数
def get_abs(n):
    if n < 0 :
        n = int(str(n).strip("-"))
        print (type(n))
    return n
def add(x,y,f):
    print(x)
    return f(x) + f(y)
print (add( 3,-10,get_abs))
