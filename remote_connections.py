
import pexpect

ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

    
def telnet():
    
    session = pexpect.spawn('telnet' + ip_address, encoding = "utf-8", timeout = 20)
    result = session.expect(['Username:', pexpect.TIMEOUT])
    
    if result != 0:
        print("Failed to create a session for: ", ip_address)
        exit()
        
    session.sendline(username)
    result = session.expect(['Password: ', pexpect.TIMEOUT])
    
    if result != 0:
        print('Failed to enter the username: ', username)
        exit()
        
    session.sendline(password)
    result - session.expect(['#', pexpect.TIMEOUT])
    
    if result != 0:
        print("Failed to enter the password: ", password)
        exit()
        
    print("Connection Established with: ", ip_address)
    print("                   Username: ", username)
    print("                   Password: ", password)
    
    session.sendline('quit')
    session.close()
    
def ssh_connection(ip_address, username, password):
    password_enable = input("Enter enable password: ")
    
    session = pexpect.spawn("ssh" + username + '@' + ip_address, encoding = 'utf-8', timeout = 20)
    result = session.expect(['Password: ', pexpect.TIMEOUT, pexpect.EOF])
    
    if result != 0:
        print("Failed to create a session for: ", ip_address)
        exit()
    
    session.sendline(password)
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
#exit enable
    session.sendline("exit")

#connection established

    print("Connection established with: ", ip_address)
    print("                   Username: ", username)
    print("                   Password: ", password)
    
#close connection
    session.close()



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