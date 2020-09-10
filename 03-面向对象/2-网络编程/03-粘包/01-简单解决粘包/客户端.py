import socket
import struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(("127.0.0.1",8083))
while True:
    mge=input("请输入内容").strip()
    if not mge :
        print ("numn")
        continue
    phone.send(mge.encode("utf-8"))
    #接受报文
    header=phone.recv(4)
    header_size=struct.unpack("i",header)[0]
    print (header_size)
    recv_size=0
    recv_data=b""
    while recv_size < header_size:
        #接收服务器返回的内容
        data=phone.recv(1024)
        recv_data+= data
        recv_size+=len(data)
        print (recv_size,"文件大小")
    print ("1111")
    print(recv_data.decode('gbk'))
phone.close
