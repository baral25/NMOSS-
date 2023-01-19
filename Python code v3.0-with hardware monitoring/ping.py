import os

ip_list = ["198.101.242.72"]
for ip in ip_list:
        response = os.popen("ping {ip}).read()")
        if "Received = 2" in response:
            print("The site is up {ip} Ping Sucessful")
        else:
            print("The site is down {ip} Ping Unsucessful")
