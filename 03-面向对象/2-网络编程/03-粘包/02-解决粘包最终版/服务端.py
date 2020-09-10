import socket
import subprocess
import struct
import json
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
            #制作固定格式报头
            header_dic={
                'filename': 'a.txt',
                'md5': 'xxdxxx',
                'total_size': len(stdout) + len(stderr)
            }
            header_json=json.dumps(header_dic)
            print (header_json)
            header_bytes=header_json.encode("utf-8")
            print (header_bytes,"111")
            #发送包头长度
            conn.send(struct.pack("i",len(header_bytes)))
            #发送报头
            conn.send(header_bytes)
            #发送正式内容内容
            conn.send(stderr+stdout)
        except ConnectionResetError: #适用于windows操作系统
            break
    conn.close()

phone.close()
