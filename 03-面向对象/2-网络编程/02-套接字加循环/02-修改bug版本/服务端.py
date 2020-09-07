import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_DONTROUTE,1)
phone.bind(("127.0.0.1",8081))
phone.listen(5)
print ("正在等待接收消息")
conn, clien_dir = phone.accept()
while True:

    print(clien_dir)
    data=conn.recv(4096)
    try:
        if not data:break
        print ("接到的消息为",data)
        conn.send(data.upper())
    except ConnectionRefusedError:
        break
conn.close()
phone.close()