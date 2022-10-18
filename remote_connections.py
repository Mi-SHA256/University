
import pexpect

ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

#telnet connection with pexpect    
def telnet():
    
    session = pexpect.spawn('telnet ' + ip_address, encoding = "utf-8", timeout = 20) #"summons" connection
    result = session.expect(['Username: ', pexpect.TIMEOUT]) #expected output, if nothing similar shows up, an error will pop up
    
    if result != 0:
        print("Failed to create a session for: ", ip_address)
        exit()
        
    session.sendline(username) #sends the previously inputted username
    result = session.expect(['Password: ', pexpect.TIMEOUT])
    
    if result != 0:
        print('Failed to enter the username: ', username)
        exit()
        
    session.sendline(password) #sends the previously inputted password
    result - session.expect(['#', pexpect.TIMEOUT])
    
    if result != 0:
        print("Failed to enter the password: ", password)
        exit()
        
    print("Connection Established with: ", ip_address)
    print("                   Username: ", username)
    print("                   Password: ", password)
    
    
    session.sendline("show running-config")
    config = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
    
    with open("running_config.txt", "w") as f:
        f.write(config)


#ssh connection with pexpect    
def ssh_connection():
    password_enable = input("Enter enable password: ")
    
    session = pexpect.spawn("ssh" + username + '@' + ip_address, encoding = 'utf-8', timeout = 20) #"summons" connection
    result = session.expect(['Password: ', pexpect.TIMEOUT, pexpect.EOF]) #expected output, if nothing similar shows up, an error will pop up
    
    if result != 0:
        print("Failed to create a session for: ", ip_address)
        exit()
    
    session.sendline(password) #sends the previously inputted password
    result = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
    
    if result != 0:
        print("Failed to enter the password: ", password)
        exit()
        
    session.sendline("enable")
    result = session.expect(['Password: ', pexpect.TIMEOUT, pexpect.EOF])
    
    if result != 0:
        print("Failed entering enable mode")
        exit()
        
    session.sendline(password_enable)
    result = session.expect(['#', pexpect.TIMEOUT, pexpect.EOF])
    
    if result != 0:
        print("Failed entering enable mode after sending the password")
        exit()
    
    session.sendline('configure terminal')
    result = session.expect([r'.\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
    
    if result != 0:
        print("Failed to enter config mode")
        exit()
        
    session.sendline("hostname R1")
    result = session.expect([r'R1\(config\)#', pexpect.TIMEOUT, pexpect.EOF])
    
    if result != 0:
        print("Failed to set a hostname")
    
#exit config
    session.sendline("exit")

#connection established

    print("Connection established with: ", ip_address)
    print("                   Username: ", username)
    print("                   Password: ", password)
    
    session.sendline("show running-config")
    config = session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
    
    with open("/home/running_config.txt", "w") as f:
        f.write(config)



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
