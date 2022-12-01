from netmiko import ConnectHandler
import getpass

print("")
ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")
secret = getpass.getpass("Enter the Secret: ")
print("")

device1 = {
    'device_type': "cisco_ios",
    'ip': ip_address,
    'username': username,
    'password': password,
    'secret': secret,    
}

connection = ConnectHandler(**device1)
connection.enable()

#the commands below are for the router R2 that was running on the IP address of 192.168.56.130 on NETLAB
commands1 = ["int lo1","ip add 1.1.1.1 255.255.255.255"]
commands2 = ["router ospf 1","network 1.1.1.1 255.255.255.0 area 0","network 2.2.2.2 255.255.255.0 area 0","network 192.168.56.130 255.255.255.0 area 0",]
commands3 = ["router eigrp 1","network 192.168.56.0"]

#for some reason netmiko dislikes using the command "exit" 
#so because netmiko automatically places the user in configure-terminal
#I found it more comfortable to reset the position after being done with an interface
#rather than finding a way of exiting the interface without crashing the program
connection.send_config_set(commands1)
connection.send_config_set(commands2)
connection.send_config_set(commands3)

r = connection.send_command("show int desc")

print("Closing Connection")
print("")
print(r)
connection.disconnect()