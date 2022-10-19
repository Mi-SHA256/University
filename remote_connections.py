
import pexpect

ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

#telnet connection with pexpect    
def telnet():
    
    session = pexpect.spawn('telnet ' + ip_address, encoding = "utf-8", timeout = 20) #"summons" connection       
    session.sendline(username) #sends the previously inputted username  
    session.sendline(password) #sends the previously inputted password
    session.sendline("show running-config")


#ssh connection with pexpect    
def ssh_connection():
    password_enable = input("Enter enable password: ")
    
    session = pexpect.spawn("ssh" + username + '@' + ip_address, encoding = 'utf-8', timeout = 20) #"summons" connection
    session.sendline(password) #sends the previously inputted password
    session.sendline("enable") #sends command to enable console
    session.sendline(password_enable)
    session.sendline("show running-config")


def menu():
    
    print("~~~~~~~~~~~~~~~~~~~~~~ Welcome! ~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please choose a way to remotely connect to a device:")
    print("")
    print("1. Telnet")
    print("2. SSH")
    print("")
    print("3. Quit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        telnet()
    elif choice == 2:
        ssh_connection()   
    elif choice == 3:
        print("Goodbye!")  
    else:
        print("Choice is not valid. ")
    
menu()
