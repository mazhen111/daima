"""2 .{‘k0’: 0, ‘k1’: 1, ‘k2’: 2, ‘k3’: 3, ‘k4’: 4, ‘k5’: 5, ‘k6’: 6, ‘k7’: 7, ‘k8’: 8, ‘k9’: 9} 请把这个dict中key大于5的值value打印出来"""

info = {"k0": 0, "k1": 1, "k2": 2, "k3": 3, "k4": 4, "k5": 5, "k6": 6, "k7": 7, "k8": 8, "k9": 9}
for i in info :
    if info[i] > 5 :
        print (i,info[i])
"""2.把题2中value是偶数的统一改成-1 """
for i in info :
    if info[i] %2 ==0 :
        info[i] = -1
print (info)
names = {
    "alex": [23, "CEO", 66000],
    "黑姑娘": [24, "行政", 4000],
}
name = input("请输入姓名").lower()
print (names.get(name))
