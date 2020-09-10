import socket
import subprocess
import struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8083)) #0-65535:0-1024给操作系统使用
phone.listen(5)

print('starting...')
while True: # 链接循环
    conn,client_addr=phone.accept()
    print(client_addr)

    while True: #通信循环
        try:
            data=conn.recv(1024)
            if not data:break #适用于linux操作系统
            job=subprocess.Popen(data.decode("gbk"),shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE
                                 )
            stdout=job.stdout.read()
            stderr=job.stderr.read()
            #发送报头
            total_size = len(stdout) + len(stderr)
            header = struct.pack('i', total_size)
            #发送报头
            print (struct.unpack("i",header))
            conn.send(header)
            #发送正式内容内容
            conn.send(stderr+stdout)
        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()

phone.close()
