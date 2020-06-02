#1, 1, 2, 3, 5, 8, 13, 21, 34, …
a,b = 0,1
count = 0

while count < 20 :
    tmp = a
    a = b
    b  =  tmp  + b
    print (b)
    count +=1