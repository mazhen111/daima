import os
import sys
import json
menu = """
账户信息
转账
提现
"""
def AccountInformation(balancepath):
    with open(balancepath)as f :
        alexformation = json.load(f)
        return alexformation
def Withdrawal(balance,balancepath,Withdrawalpath,Bankbalance):
    """"
    balance alex 账户余额
    balancepath   alex 账户余额json
    Withdrawalpath 银行账户json
    Bankbalance 银行余额
    """
    consumption = int(input("请输入消费的金额").strip())
    print (balance["balance"] - (consumption + (consumption * 0.05)))
    balance["balance"]=balance["balance"] - (consumption + (consumption * 0.05))
    Bankbalance["balance"]=Bankbalance["balance"]+ (consumption + (consumption * 0.05))
    print (Bankbalance,balance)
    with open(balancepath,"w") as f :
        json.dump(balance,f)
    with open(Withdrawalpath,"w") as f :
        json.dump(Bankbalance,f)

def withdrawal(balance,balancepath):
    withdrawalamount = int(input("请输入提现额度"))
    print (balance["CreditLimit"])
    if balance["CreditLimit"]  >  withdrawalamount:
        balance["balance"] = balance["balance"] + (withdrawalamount - (withdrawalamount * 0.05))
        balance["CreditLimit"] =  balance["CreditLimit"] - withdrawalamount
        print (balance)
        with open(balancepath,"w") as f :
            json.dump(balance,f)

    else:
        print ("信用不足，请联系银行")
print (""" ———- ICBC Bank ————-""")
for i,n in enumerate(menu.split()):
    print (i+1,n)
while True :
    SerialNumber = input("请输入序号").strip()
    if SerialNumber.isdigit() and  len(menu.split()) >= int(SerialNumber):
        if SerialNumber == "1":
            print (AccountInformation("../account/alex.json"))
        elif SerialNumber == "2" :
            Withdrawal(AccountInformation("../account/alex.json"),"../account/alex.json","../account/tesla_company.json",AccountInformation("../account/tesla_company.json"))
        elif  SerialNumber == "3" :
            withdrawal(AccountInformation("../account/alex.json"),"../account/alex.json")
    else:
        print ("输入的非法字符")