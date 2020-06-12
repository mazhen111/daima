import json
import hashlib

def get_md5(data):
    obj = hashlib.md5()
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result
with open("account.json") as f :
    account = json.load(f)
print (account["password"])
print(get_md5(account["password"]))
mun = 0
while mun < 3  :
    if account["status"] == 0:
        user = input("请输入账号").strip()
        passwd = input("请输入密码").strip()
        passwdmd5 = get_md5(passwd)
        print (passwdmd5)
        if user == "mazhen"  and  passwdmd5 ==get_md5(account["password"]) :
            print ("登录成功")
            exit()
        mun += 1
        if mun ==3 :
            account["status"]=1
            print (account,"用户已锁定")
            with open("account.json","w")as f :
                json.dump(account,f)

    else:
        print ("用户锁定")
        exit()






