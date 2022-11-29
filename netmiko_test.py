import netmiko 

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
    
#for testing this code I have used the Netlab Open Lab machines
#before running the code I set the usernames and passwords to "cisco"


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
        print('79')
        net_connect.send_config_set(commands)
        print('81')

    result = net_connect.send_show_command(device1, ["sh clock", "sh ip int br"])
    print('84')
    print(result, width=120)


def menu():
    choice = int(input("1 is no file, 2 is file: "))
    if choice == 1:
        netmiko_loopback()
        print("netmiko_loopback")
    elif choice == 2:
        netmiko_loopback_file()
        print("netmiko_loopback_file")
    else:
        return 0
    
menu()
    
