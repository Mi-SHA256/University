# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pexpect 


ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = input("Enter Password: ")


#def int_sum(ip, username, password):
    
#    session = pexpect.spawn('telnet ' + ip_address, encoding = "utf-8", timeout = 20) #"summons" connection       
#    session.expect(["Username:", pexpect.TIMEOUT])
    
#    session.sendline(username) #sends the previously inputted username  
#    session.expect(["Password:", pexpect.TIMEOUT])
    
#    session.sendline(password) #sends the previously inputted password
#    session.expect(["#", pexpect.TIMEOUT])
    
#    session.sendline("show interface summary")
#    session.expect(["#", pexpect.TIMEOUT])
    
#    print("Showing Interface Output")
#    print("-------------------------------------------------")
#    print(session.before)
    
    
def device_info():
    
    name = input("Enter the name of the file you want to open: ")
    
    dev_list = []
    file = open(name, 'r')
    for line in file:
    
        dev_info_list = line.strip().split("2")
        
        dev_info = {}
        dev_info ['name'] = dev_info_list[0]
        dev_info ['ip'] = dev_info_list[1]
        dev_info ['username'] = dev_info_list[2]
        dev_info ['password'] = dev_info_list[3]
        
        dev_list.append[dev_info]
        
    return dev_list

def print_info(device_info, int_sum):
    
    print("--------------------------------------------------------------------")
    print(" Device Name: ", device_info['name'])
    print(" Device IP  : ", device_info['ip'])
    print(" Device User: ", device_info['username'])
    print(" Device Pass: ", device_info['password'])
    
    print("")
    print("                  Showing Interface Brief ")
    print("")
    
    print(int_sum)
    print("--------------------------------------------------------------------")