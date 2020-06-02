def fib(max):
    a, b = 0, 1
    count = 0
    while  count < max :
        tmp = a
        a = b
        b = tmp + b
        yield  b
        print (a,b)
        count += 1

f = fib(20)
print (f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())