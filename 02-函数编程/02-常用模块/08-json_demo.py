import json
# data = {'k1':123,'k2':'Hello'}
# with open("p.json","w") as f:
#     json.dump(data,f)
f = open("p.json","r")
print (json.load(f))


