import os.path
import sys

#checking IP address file and content validity
def ip_file_valid():
    #Prompet user for input
    ip_file = input('\n# Enter IP file path and name (e.g. D:\MyApps\myfile.txt): ')

    #checking if the file exists
    if os.path.isfile(ip_file) == True:
        print("\n* IP file is valid :\n")
    else:
        print(f'\n* File {ip_file} does not exist :')
    #Open user selected file for reading (IP addreses file)
    selected_ip_file = open(ip_file, 'r')
    #Starting from the beginning of the File
    selected_ip_file.seek(0)

    #Reading each line (IP Address) in the File
    ip_list = selected_ip_file.readlines()

    #closing the File
    selected_ip_file.close()
    return ip_list
