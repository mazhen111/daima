import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(("127.0.0.1",8081))
while True:
    mge=input("请输入内容").strip()
    if not mge :
        print ("numn")
        continue
    phone.send(mge.encode("utf-8"))
    #接收服务器返回的内容
    data=phone.recv(1024)
    print ("返回的内容",data)
phone.close
