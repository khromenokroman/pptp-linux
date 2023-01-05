#! /usr/bin/python3
#это все можно поместить в планировщик crontab -e
#например так
#*/1 * * * * /home/dima/ppptp-scripts/pptp.sh

import os

result = os.system('ping -Q 2 -c 4 -t 2 192.168.221.1')
if result != 0:
    os.system('killall pppd')
    os.system('pppd call vpn-unix')
else:
    print('ok')
