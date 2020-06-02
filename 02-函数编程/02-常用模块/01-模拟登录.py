import paramiko
import os
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('116.85.64.201', 22, 'root', 'Zhen19931106')
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.read())
ssh.close()
print (__file__)
print (os.path.abspath(__file__))
