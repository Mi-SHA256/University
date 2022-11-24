from netmiko import ConnectHandler #imported connecthandler from the netmiko library
import pexpect #imported pexpect library to help with connections
import difflib #imported difflib library to compare files


#telnet connection with pexpect    
def telnet():
    
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    
    session = pexpect.spawn('telnet ' + ip_address, encoding = "utf-8", timeout = 20) #"summons" connection       
    session.expect(["Username:", pexpect.TIMEOUT])
    
    session.sendline(username) #sends the previously inputted username  
    session.expect(["Password:", pexpect.TIMEOUT])
    
    session.sendline(password) #sends the previously inputted password
    session.expect(["#", pexpect.TIMEOUT])
    
    session.sendline("show user")
    session.expect(["#", pexpect.TIMEOUT])
    
    print(session.before)




#ssh connection with pexpect    
def ssh_connection():
    
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")    
    password_enable = input("Enter enable password: ")
    
    session = pexpect.spawn("ssh " + username + '@' + ip_address, encoding = 'utf-8', timeout = 20) #"summons" connection
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

    
    session.sendline(password) #sends the previously inputted password
    session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("enable") #sends command to enable console
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline(password_enable)
    session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline("show user")
    session.expect(["#", pexpect.TIMEOUT])
    
    print(session.before)

def ssh_config():
    
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    password_enable = input("Enter enable password: ")
    
    session = pexpect.spawn("ssh " + username + '@' + ip_address, encoding = 'utf-8', timeout = 20) #"summons" connection
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

    
    session.sendline(password) #sends the previously inputted password
    session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("enable") #sends command to enable console
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline(password_enable)
    session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline("terminal length 0")
    session.expect(["#", pexpect.TIMEOUT])
    
    session.sendline("show run")
    session.expect(["#", pexpect.TIMEOUT])
    

    with open("config_ssh.txt", "w") as f:
        f.write(session.before)
        f.close()
    print("The running configuration has been saved to config_ssh.txt")

def ssh_config_compare():
    
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    
    password_enable = input("Enter enable password: ")

    session = pexpect.spawn("ssh " + username + '@' + ip_address, encoding = 'utf-8', timeout = 20) #"summons" connection
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

    session.sendline(password) #sends the previously inputted password
    session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])

    session.sendline("enable") #sends command to enable console
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline(password_enable)
    session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline("terminal length 0") #makes the terminal's limit null, allowing the console to display everyting on one singular page
    session.expect(["#", pexpect.TIMEOUT])
    
    session.sendline("show archive config diff")
    session.expect(["#", pexpect.TIMEOUT])
    
    print(session.before)


def ssh_compare_online_with_offline():
    
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    file_name = input("Please input the filename of the file you wish to compare to the running config(MUST INCLUDE EXTENSION): ")
    
    session = pexpect.spawn("ssh " + username + '@' + ip_address, encoding = 'utf-8', timeout = 20) #"summons" connection
    session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])

    session.sendline(password) #sends the previously inputted password
    session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
    
    session.sendline("terminal length 0")
    session.expect(["#", pexpect.TIMEOUT])
    
    session.sendline("show run")
    session.expect(["#", pexpect.TIMEOUT])

    with open("running_config_ssh.txt", "w") as f:
        f.write(session.before)
        f.close()

#guides for the user
    print("")
    print(' - Line unique to file 1')
    print(' + Line unique to file 2')
    print('   Line common in both files')
    print(' ? Line not present in either files')
    print("")
    
    with open("running_config_ssh.txt", "r") as file1:
        text1 = file1.readlines()
    with open(file_name, "r") as file2:
        text2 = file2.readlines()
    
    for line in difflib.unified_diff(
            text1, text2, fromfile ='running_config_ssh.txt',
            tofile = file_name, lineterm=''):
            print(line)

def netmiko_loopback_file():
        
    print("WARNING! THIS REQUIRES AN EXTERNAL FILE WITH THE COMMANDS YOU WISH TO USE!")
    print("")
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    device = input("Enter the device type(IOS): ")
    print("")
    config_file = input("Enter the name of the file with the config commands(file extension too): ")
    
    device1 = {
        'device_type': device,
        'ip': ip_address,
        'username': username,
        'password': password,
        
        }
    
    with open(config_file) as w:
        line = w.read().splitlines()
    print (line)
    
    all_devices = [device1]
    
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(line)
        print(output)
    

def netmiko_loopback():
    
    print("---WARNING! THIS HAS PRESET COMMANDS WITHIN THE CODE ITSELF!---")
    print(" ---IF YOU WISH TO CHANGE THEM YOU HAVE TO MANUALLY DO SO!---")
    print("")
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    device = input("Enter the device type(IOS): ")
    print("")
    
    device1 = {
        'device_type': device,
        'ip': ip_address,
        'username': username,
        'password': password,
        
        }
    
    all_devices = [device1]
    
    
    commands = ["enable",
                "conf t",
                "int lo1",
                "ip add 1.1.1.1 255.255.255.255",
                "exit",
                
                "router ospf 1",
                "network 1.1.1.1 255.255.255.0 area 0",
                "network 2.2.2.2 255.255.255.0 area 0",
                "network 192.168.56.103 255.255.255.0 area 0",
                "exit",
                
                "router eigrp 1",
                "network 192.168.56.0",
                "end",
                "wr",
                "exit"]
    
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        net_connect.send_config_set(commands)

    result = net_connect.send_show_command(device1, ["sh clock", "sh ip int br"])
    print(result, width=120)

def menu(): #menu that will prompt up once the user starts the script/program
    
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~ Welcome! ~~~~~~~~~~~~~~~~~~~~~~~")
    print("               Please choose an option")
    print("")
    print("1. Telnet")
    print("2. SSH")
    print("3. Save config file via secure connection")
    print("4. Compare running and startup config")
    print("5. Compare running config to backed-up file")
    print("6. Configure IP and Loopback with file")
    print("7. Configure IP and Loopback without file")
    print("")
    print("8. Quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        telnet()
    elif choice == 2:
        ssh_connection()
    elif choice == 3:
        ssh_config()   
    elif choice == 4:
        ssh_config_compare()
    elif choice == 5:
        ssh_compare_online_with_offline()
    elif choice == 6:
        netmiko_loopback_file()
    elif choice == 7:
        netmiko_loopback()
    elif choice == 8:
        print("Goodbye!")  
    else:
        print("Choice is not valid. ")
    
menu()
