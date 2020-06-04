#pickle，用于python特有的类型 和 python的数据类型间进行转换
import pickle
# data = {'k1':123,'k2':'Hello'}
# p_str = pickle.dumps(data)
# print (p_str)
# with open("p.pk","wb") as f :
#     pickle.dump(data,f)
f = open("p.pk","rb")
print (pickle.load(f))