#!/usr/bin/env python
import psutil
import os
import speedtest


# # gives a single float value

# # gives an object with many fields
# psutil.virtual_memory()
# # you can convert that object to a dictionary 
# dict(psutil.virtual_memory()._asdict())
# # you can have the percentage of used RAM
# psutil.virtual_memory().percent
# 79.2
# # you can calculate percentage of available memory
# psutil.virtual_memory().available * 100 / psutil.virtual_memory().total
# 20.8

# print('memory % used:', psutil.virtual_memory()[2])
# print('cpu % used:',psutil.cpu_percent(1), '%')
# print(psutil.users())
# print(psutil.net_io_counters(1))
# import socket
# host_name = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
# print(host_ip)
# print(host_name)
st= speedtest.Speedtest()
print('My download speed is:', st.download())

