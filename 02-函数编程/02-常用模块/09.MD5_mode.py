import hashlib
m = hashlib.md5()
m.update(b" mazhen")
print (m.hexdigest())
m.update("mahen".encode("utf-8"))
print (m.hexdigest()) # 返回16进制格式的hash值
#主要提供 SHA1, SHA224, SHA256,
m1 = hashlib.sha3_256()
m1.update("mazhen妈妈妈妈".encode("utf-8"))
print (m1.hexdigest())
