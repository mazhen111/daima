import os
file_name = "兼职白领学生空姐模特护士联系方式.txt"
new_file_name = "%s.new"%(file_name)
old_str = "黑姑娘2"
new_str = "mazhen"
f = open(file_name ,"r")
f_wew = open(new_file_name ,"w")
for i in f:
    if old_str in i :
        new_line = i.replace(old_str,new_str)
        print (new_line)
    else :
        new_line = i
    f_wew.write(new_line)
f.close()
f_wew.close()
os.replace(new_file_name,file_name)