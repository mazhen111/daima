f = open("win_data.txt","rb")
f_file  = f.read()
f.close()
f_GDK = f_file.decode("UTF-8").encode("GBK")
f_wite = open("win_data.txt","wb")
f_wite.write(f_GDK)
f_wite.close()