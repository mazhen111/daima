import socket
import struct
import  json
download_dir=r'D:\python代码\daima\03-面向对象\2-网络编程\04-文件传输\1_普通版本\client\download'
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(("127.0.0.1",8084))
while True:
    mge=input("请输入内容").strip()
    if not mge :
        print ("numn")
        continue
    phone.send(mge.encode("utf-8"))
    #接受报文长度
    header=phone.recv(4)
    header_length=struct.unpack("i",header)[0]
    #收报头信息
    header_bytes=phone.recv(header_length)
    header_json=json.loads(header_bytes.decode("utf-8"))
    header_size=header_json["total_size"]
    filename=header_json["filename"]
    print (header_size)
    print (filename)
    print (download_dir)
    recv_size=0

    with open(r'%s\%s' %(download_dir,filename),"wb")as f:

        while recv_size < header_size:
        #接收服务器返回的内容
            data=phone.recv(1024)
            f.write(data)
            recv_size+=len(data)
            print (recv_size,"文件大小")
phone.close
