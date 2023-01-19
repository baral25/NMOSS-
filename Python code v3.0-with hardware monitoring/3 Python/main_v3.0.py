import datetime
from datetime import date
import time
import subprocess 
import socket  
import string
import os
import sys
import re
import psutil
import platform
import pyfiglet
import webbrowser
# #################################
# #for LOGO
# #################################
logo_1 = pyfiglet.figlet_format("NMOSS ", font = "slant"  ) 
print(logo_1)
print("")
time.sleep(0.7)
logo_2 = pyfiglet.figlet_format("NETWORK", font = "slant"  ) 
print(logo_2)
print("")
time.sleep(0.7)
logo_3 = pyfiglet.figlet_format("Monitor", font = "slant"  ) 
print(logo_3)
print("")
logo_4 = pyfiglet.figlet_format("V_3.0", font = "slant"  ) 
print(logo_4)
print("")
time.sleep(0.7)
####################################################
#this is for the cration of a new txt file with every execution of the script
####################################################
timestr = time.strftime("%Y_%m_%d-%I_%M_%S_%p")
c_dir= os.getcwd()
os.chdir(c_dir)
def get_filename_datetime():
    # Use current date to get a text file name.
    return "log--" + timestr + ".txt"

# Get full path for writing.

name = get_filename_datetime()
path = c_dir+ name
print("="*40, "Log File Details", "="*40)
print("| NAME   : ", name)
print("")
print("| PATH   :", path)
print("="*90)
time.sleep(0.7)
#################################
#for CMD Commands
#################################
print("")
print("YOUR RELEVANT INFORMATION IS LOADING.....")
os.popen("netstat -o>netstat.txt")
time.sleep(5)
#pqbar.update(10)

os.popen("netsh wlan sh int>wlan.txt")
time.sleep(2)

os.popen("ipconfig>ipconfig.txt")
time.sleep(1)

os.popen("nslookup>nslookup.txt")
time.sleep(2)

os.popen("netsh wlan show networks mode = bssid >networks.txt")
time.sleep(3)
os.popen("tasklist>tasklist.txt")

os.popen("netsh wlan show profiles>profiles.txt")
time.sleep(1)

os.popen("netstat -r>tables_net.txt")
###################
#FOR /L %i IN (1,1,254) DO ping -n 1 192.168.10.%i | FIND /i "Reply">>ipaddresses.txt
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)
print("")
print("="*40, "Quick Info", "="*40)
    
print("Your Computer Name is      :" + hostname) 
print("")   
print("Your Computer IP Address is:" + IPAddr) 

print("")   
time.sleep(0.7)
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print("="*40, "CPU Info", "="*40)
# number of cores
time.sleep(0.3)
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
print("-"*40) 
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
time.sleep(0.7)
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
time.sleep(0.7)
# Network information
print("="*40, "Network I/O Since Boot", "="*40)
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
time.sleep(0.7)
# s=speedtest.Speedtest()
# print('My download speed is:', s.download())
print("="*40, "Process Monitor", "="*40)
process_table = PrettyTable(['PID', 'PNAME', 'STATUS','CPU', 'NUM THREADS'])
for process in psutil.pids()[-20:]:

        # While fetching the processes, some of the subprocesses may exit 
        # Hence we need to put this code in try-except block
        try:
            p = psutil.Process(process)
            process_table.add_row([
                str(process),
                p.name(),
                p.status(),
                str(p.cpu_percent())+"%",
                p.num_threads()
                ])
              
        except Exception as e:
            pass
print(process_table)
  
    # Create a 1 second delay
time.sleep(1)

logo_5 = pyfiglet.figlet_format("Cmd Info", font = "slant"  ) 
print(logo_5)



################################
#For Devices in Network
################################
#only displayed information
print("")
print("---------------------------------")
print("Arp- Table for Network           ")
print("---------------------------------")
arp_table = subprocess.check_output(['netstat','-r']) 
# decode it to strings 
arp_table = arp_table.decode('ascii') 
arp_table= arp_table.replace("\r","") 
# displaying the information 
print(arp_table)
print("")
print("-------------------------------")
print("SCANNING CONNECTIONS IN NETWORK")
print("-------------------------------")
for i in tqdm(range(0, 25), unit =" ticks",  
              desc ="Scanning For Devices In Network"): 
            time.sleep(0.1)
request = scapy.ARP() 	
request.pdst = IPAddr+'/24'
broadcast = scapy.Ether() 
    
broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    
request_broadcast = broadcast / request 
clients = scapy.srp(request_broadcast, timeout = 10,verbose = 1)[0]
print("") 
print("IP_ADDRESS          MAC_ADDRESS")
print("")
for element in clients: 
    print(element[1].psrc + "	 " + element[1].hwsrc )
    
  
# Function to get the interface name 

print("")
print("----------------------------------------")
print("CONNECTIONS IN NETWORK WIHT VENDOR NAMES")
print("----------------------------------------")
def get_mac_details(mac_address): 
    
    
    url = "https://api.macvendors.com/"
    time.sleep(2)
    
    
    response = requests.get(url+element[1].hwsrc) 
    if response.status_code != 200: 
        print("Unknown Mac Address")
    return response.content.decode() 

print("")
print("[+] Checking Mac Addresses for IP's in Network...") 
print("")
if __name__ == "__main__": 

    for element in clients:
        vendor_name = get_mac_details(element[1].hwsrc) 
        print("[+] Device vendor for" + "  "+element[1].psrc + "  " + "with MAC ADD" + "  "+ element[1].hwsrc+ "  "+ "is:"+ "  "  +vendor_name)
        org_std=sys.stdout
        with open(path,"a") as f:
            sys.stdout=f
            print("[+] Device vendor for" + "  "+element[1].psrc + "  " + "with MAC ADD" + "  "+ element[1].hwsrc+ "  "+ "is:"+ "  "  +vendor_name)
            sys.stdout=org_std 

#########################################################
#this is to write data on thus created file
#########################################################   

errors = []
bad_chars=[',',"[","]", "(" , ")", " '", "''"]
linenum = 0
print("")
#print("##########Your netstat information#########")
print("----------------------------------------------------------------------------")
print(" Protocol     Address                    Device            Status      PID")
print("----------------------------------------------------------------------------")
pattern = re.compile("established", re.IGNORECASE)  # Compile a case-insensitive regex
with open ('netstat.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
time.sleep(0.7)           
for err in errors:                            # Iterate over the list of tuples
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)       
############################################
#For Searching driver in the txt file of wlan
############################################
errors = []
bad_chars=[',',"[","]", "(" , ")", " '", "''"]
linenum = 0
print("")
print("-------------------------------")
print("Wireless Connection Information")
print("-------------------------------")
pattern = re.compile("description", re.IGNORECASE)  # Compile a case-insensitive regex
with open ('wlan.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
             
for err in errors:                            # Iterate over the list of tuples
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)
    time.sleep(0.7)  
############################################
#For Searching SSID AND BSSID from wlan.txt
############################################      
errors = []
bad_chars=[',',"[","]", "(" , ")", " '", "''"]
linenum = 0

pattern = re.compile("SSID")  # Compile a case-insensitive regex
with open ('wlan.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
             
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)
    time.sleep(0.7)
############################################
#For Searching radio type from wlan.txt
############################################      
errors = []
linenum = 0
pattern = re.compile("Radio type")  # Compile a case-insensitive regex
with open ('wlan.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)
   
############################################
#For Searching Authentication in Wlan.txt
############################################      
errors = []
linenum = 0
pattern = re.compile("Authentication")  # Compile a case-insensitive regex
with open ('wlan.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)
    
############################################
#For Searching channel in wlan.txt
############################################      
errors = []
linenum = 0
pattern = re.compile("Channel")  # Compile a case-insensitive regex
with open ('wlan.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors: # Iterate over the list of tuples   
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)
    
  
############################################
#For signal strength in wlan.txt
############################################      
errors = []
linenum = 0
pattern = re.compile("Signal")  # Compile a case-insensitive regex
with open ('wlan.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f) 
############################################
#For ip-address both ipv4 and ipv6
############################################      
errors = []
linenum = 0
print("")
print("-----------------------")
print("IPv4 & IPv6 INFORMATION")
print("-----------------------")
pattern = re.compile("Address")  # Compile a case-insensitive regex
with open ('ipconfig.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f) 
  
############################################
#For subnet mask
############################################      
errors = []
linenum = 0
pattern = re.compile("Subnet mask")  # Compile a case-insensitive regex
with open ('ipconfig.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)  
 
############################################
#For default gateway
############################################      
errors = []
all_around = ()
linenum = 0
pattern = re.compile("Default Gateway")  # Compile a case-insensitive regex
with open ('ipconfig.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f) 
   
############################################
#For nslookup (server)
############################################      
errors = []
linenum = 0
print("")
print("-----------------")
print("ISP DNS SERVER...")
print("-----------------")
pattern = re.compile("Default Server")  # Compile a case-insensitive regex
with open ('nslookup.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
   
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)      
############################################
#For nslookup (address)
############################################      
errors = []
linenum = 0
pattern = re.compile("Address")  # Compile a case-insensitive regex
with open ('nslookup.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    time.sleep(0.7)
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)  

############################################
#For netsh show networks mode = BSSID (search SSID)
############################################      
#errors = []
#linenum = 0
print("")
print("---------------------------------")
print("NEIGHBOURING NETWORKS INFORMATION")
print("---------------------------------")
devices = subprocess.check_output(['netsh','wlan','show','network','mode', '=','bssid']) 
# decode it to strings 
devices = devices.decode('ascii') 
devices= devices.replace("\r","") 
# displaying the information 
print(devices)
with open(path, "a") as f:
      
      f.write(devices)

############################################
#For netsh show networks mode = BSSID (search Signal)
############################################      
errors = []
linenum = 0
print("")
print("----------------------")
print("LAST CONNECTED NETWORK")
print("----------------------")
pattern = re.compile("All User Profile")  # Compile a case-insensitive regex
with open ('profiles.txt', 'rt') as myfile:    
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:      # If a match is found 
            output = errors.append(line.split('\n'))
for err in errors:                            # Iterate over the list of tuples
    print("" + str(err[0])  +str(err[1]))
    with open(path, "a") as f:
     print("" + str(err[0])  +str(err[1]),file=f)
    break   
################################
#For Display only Doesnt write to log file
################################
print("")  
print("")        
for i in tqdm(range(0, 25), unit ="ticks",  
              desc ="Creating Log File"): 
            time.sleep(0.1)

# tasklist
print("")            
print("Log File created with name:", name)            
print("")
print("Log File can be found in path:", path)
print("")
print("UPLOAD THE TEXT FILE TO OUR WEBSITE FOR FURTHER ANALYSIS")
print("")
input("Press Enter to continue to website or Ctrl+C to exit.") 
webbrowser . open('https://pedantic-minsky-d0f88a.netlify.app/file_reader.html')
