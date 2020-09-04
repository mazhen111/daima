import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#打电话
phone.connect(("127.0.0.1",8080))

#手发消息
phone.send("mazhen".encode("utf-8"))
data=phone.recv(1024)
print ("返回的数据",data)
phone.close()