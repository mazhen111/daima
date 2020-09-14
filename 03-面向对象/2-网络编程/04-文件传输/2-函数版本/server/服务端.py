import socket
import subprocess
import struct
import json
import os
share_dir=r'D:\python代码\daima\03-面向对象\2-网络编程\04-文件传输\2-函数版本\server\share'
print (share_dir)


def get (conn,mge):
    filename = mge[1]
    filename = filename.decode("utf-8")

    # 制作固定格式报头
    header_dic = {
        'filename': filename,
        'md5': 'xxdxxx',
        'total_size': os.path.getsize(r'%s\%s' % (share_dir, filename))
    }
    header_json = json.dumps(header_dic)
    print(header_json)
    header_bytes = header_json.encode("utf-8")
    print(header_bytes, "111")
    # 发送包头长度
    conn.send(struct.pack("i", len(header_bytes)))
    # 发送报头
    conn.send(header_bytes)
    # 发送正式内容内容
    with open(r'%s/%s' % (share_dir, filename), "rb") as f:
        for line in f:
            conn.send(line)



def run():
    print('starting...')
    phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    phone.bind(('127.0.0.1', 8084))  # 0-65535:0-1024给操作系统使用
    phone.listen(5)
    while True: # 链接循环
        conn,client_addr=phone.accept()
        print(client_addr)

        while True: #通信循环
            try:
                data=conn.recv(1024)
                if not data:break #适用于linux操作系统
                mge=data.split()
                print ("111")
                filename=mge[1]
                cmd=mge[0]
                print (cmd)
                if cmd.decode("utf-8") == "get":
                    get(conn,mge)
                else:
                    print ("输入不正确")


            except ConnectionResetError: #适用于windows操作系统
                break
        conn.close()

    phone.close()

if __name__=="__main__":
    run()
