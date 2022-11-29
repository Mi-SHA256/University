from netmiko import ConnectHandler
import getpass

def netmiko_loopback_file():
        
    print("WARNING! THIS REQUIRES AN EXTERNAL FILE WITH THE COMMANDS YOU WISH TO USE!")
    print("")
    print("Details for the 1st device")
    ip_address = input("Enter IP address: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    secret = input("Enter Secret: ")

    print("Details for the 2nd device")
    ip_address1 = input("Enter IP address: ")
    username1 = input("Enter Username: ")
    password1 = input("Enter Password: ")
    secret1 = input("Enter Secret: ")

    print("")
    config_file = input("Enter the name of the file: ")
    
    device1 = {
        'device_type': "cisco_ios",
        'ip': ip_address,
        'username': username,
        'password': password,
        'secret' : secret,
        }
    
    device2 = {
        'device_type': "cisco_ios",
        'ip': ip_address1,
        'username': username1,
        'password': password1,
        'secret': secret1,
    }


    with open(config_file) as w:
        line = w.read().splitlines()
    print (line)
    
    all_devices = [device1,device2]
    
    for devices in all_devices:
        net_connect = ConnectHandler(**devices)
        output = net_connect.send_config_set(line)
        print(output)
    