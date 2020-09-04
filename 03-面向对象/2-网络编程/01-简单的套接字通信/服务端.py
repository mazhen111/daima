import socket
#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定手机卡
phone.bind(("127.0.0.1",8080))
#3开机
phone.listen(5)
#4等待打电话
print ("starting...")
conn,cline_addr=phone.accept()

#5收发消息
data=conn.recv(1024)
print('客户端的数据',data)
conn.send(data.upper())
conn.close()
phone.close()