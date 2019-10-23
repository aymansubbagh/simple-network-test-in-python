import sys

#checking octets
def ip_addr_valid(list):

    #Iterating over the list of ip
    for ip in list:
        ip = ip.strip('\n')
        octet_list = ip.split('.')

        if (len(octet_list) == 4 ) and (1 <= int(octet_list[0]) <= 223) and ( int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and  (0 <= int(octet_list[1]) <=255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
        else:
            print(f'\n* There was an invalid IP address in the file: {ip} :(\n')
            sys.exit()
