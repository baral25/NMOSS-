import os
os.chdir(r'D:\Desktop\Final Year 1st Sem\Python\file.txt')
os.popen("netsh wlan sh int>wlan.txt")
os.popen("ipconfig>ipconfig.txt")
os.popen("netstat -a -o>netstat.txt")
