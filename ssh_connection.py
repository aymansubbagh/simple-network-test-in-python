import paramiko
import os.path
import time
import sys
import re


#checking username/password File
#prompting user for input - USERNAME/PASSWORD FILE
user_file = input('\n# Enter user file path and name (e.g. D:\MyApps\myfile.txt): ')

#Verifying the validity of the username/password File
if os.path.isfile(user_file) == True:
    print('\n* User/Password file is valid :)\n')

else:
    print(f'\n* File {user_file} deos not exist :( Please check and try again.\n')
    sys.exit()

#checking commands File
#prompting user for input - COMMANDS FILE
cmd_file = input('\n# Enter commands file path and name (e.g. D:\MyApps\myfile.txt): ')

#Verifying the validity of the commands File
if os.path.isfile(user_file) == True:
    print('\n* commands file is valid :)\n')

else:
    print(f'\n* File {cmd_file} deos not exist :( Please check and try again.\n')
    sys.exit()

def ssh_connection(ip):
    global user_file
    global cmd_file

    #Creating SSH connection
    try:
        #Define SSH parameters
        selected_user_file = open(user_file, 'r')

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the username from the file
        username = selected_user_file.readlines()[0].split(',')[0].strip('\n')

        #Starting from the beginning of the file
        selected_user_file.seek(0)

        #Reading the password from the file
        password = selected_user_file.readlines()[0].split(',')[1].strip('\n')

        #Logging inyo device
        session = paramiko.SSHClient()

        #For testing puposes, this allows auto-accepting unknown host keys
        #DO NOT USE IN PRODUCTION! the default would be RejectPolicy
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the device using username and password
        session.connect(ip.strip('\n'), username = '', password = '')

        #Start an interactive shell session on the router
        connection = session.invoke_shell()

        #Setting terminal length for entire output - disable pagination
        connection.send('enable\n')
        connection.send('terminal length 0\n')
        time.sleep(1)

        #Entering global config mode
        connection.send('\n')
        connection.send('configure terminal\n')
        time.sleep(1)

        #Open user selected file for Reading
        selected_cmd_file = open(cmd_file, 'r')
        #Startingfrom the beginning
        selected_cmd_file.seek(0)

        #Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line+'\n')
            time.sleep(2)
        #Closing the user file
        selected_user_file.close()

        #Closing the commad file
        selected_cmd_file.close()

        #checking the command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b'% Invalid input', router_output):
            print(f'* There was at least one IOS syntax erros on the device {ip}')
        else:
            print(f'\nDone for device {ip}')
        #Test for reading command output
        #print(re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', str(router_output)))

        #Closing the connection
        session.close()
    except paramiko.AuthenticationException:
        print('* Invalid username or password, please check the username/password file')
        print('* Closing program... Bye!')
