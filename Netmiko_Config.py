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

connection = connectHandler(**device1)
connection.enable()

#the commands below are for the router that was running on the IP address of 192.168.56.130 on NETLAB
commands = ["enable","conf t","int lo1","ip add 1.1.1.1 255.255.255.255","exit","router ospf 1","network 1.1.1.1 255.255.255.0 area 0","network 2.2.2.2 255.255.255.0 area 0","network 192.168.56.103 255.255.255.0 area 0","exit","router eigrp 1","network 192.168.56.0","end","wr","exit"]
connection.send_config_set(commands)

r = connection.send_command("show int desc")

print("Closing Connection")
print("")
print(r)
connection.disconnect()