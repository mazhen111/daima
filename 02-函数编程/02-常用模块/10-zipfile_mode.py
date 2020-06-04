import shutil
import zipfile
import os
z = zipfile.ZipFile("MA.zip","w")
filelist = []
for root_dir,dirs ,file in os.walk("../02-常用模块"):
    for i in file:
        filelist.append(os.path.join(root_dir,i))
for i in filelist:
    print (i)
    z.write(i)
z.close()