import sys
import subprocess

#checking IP reachability
def ip_reach(list):
    for ip in list:
        ip = ip.strip("\n")
        #print(f'ip->{ip}')
        ping_reply = subprocess.call(f'ping {ip}', stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_reply == 0:
            print(f'\n* {ip} is reachable:)\n')
            continue
        else:
            print(f'\n* {ip} is not reachable :) Check connectivity and try again.')
            sys.exit()
