#现有列表a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],要求你把列表里的每个值加1
a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for index,i in enumerate(a) :
#     a[index] += 1
# print (a)

#l列表生成器a
a = [i + 3  for i in a]
print (a)