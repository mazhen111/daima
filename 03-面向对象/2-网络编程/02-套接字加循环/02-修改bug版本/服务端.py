import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_DONTROUTE,1)
phone.bind(("127.0.0.1",8081))
phone.listen(5)
print ("正在等待接收消息")

while True:
    conn, clien_dir = phone.accept()
    print(clien_dir)
    data=conn.recv(4096)
    if not data:
         print ("收到消息为空")
         continue
    print ("接到的消息为",data)
    conn.send(data.upper())
conn.close()
phone.close()