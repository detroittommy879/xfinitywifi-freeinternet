#!/usr/bin/python3

import subprocess
import time
import random

wifid = 'testwifiadaptername'

# wifid='wlxc83a35c2dd6b'my actual adapter name

mac = ':'.join(("%12x" % random.randint(0, 0xFFFFFFFFFFFF))[i:i+2] for i in range(0, 12, 2))

print("New mac address will be " + mac)

com1 = "ip link set dev " + wifid + " up"
com2 = "ip link set dev " + wifid + " down"
com3 = "macchanger -m " + mac + " " + "wifid"

subprocess.run(com2, shell=True)
time.sleep(3)
subprocess.run(com3, shell=True)
time.sleep(3)
subprocess.run(com1, shell=True)

# subprocess.run('ip', 'link', 'set', 'dev' , wifid, ' down')

# print(com1)
# print(com2)
# print(com3)
# macchanger -m 32:cf:cb:00:dd:f1 wlxc83a35c2dd6b
