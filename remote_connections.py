
import pexpect

ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

#telnet connection with pexpect    
def telnet():
    
    session = pexpect.spawn('telnet ' + ip_address, encoding = "utf-8", timeout = 20) #"summons" connection       
    session.expect(["Username:", pexpect.TIMEOUT])
    
    session.sendline(username) #sends the previously inputted username  
    session.expect(["Password:", pexpect.TIMEOUT])
    
    session.sendline(password) #sends the previously inputted password
    session.expect(["#", pexpect.TIMEOUT])
    
    session.sendline("terminal length 0")
    session.expect(["#", pexpect.TIMEOUT])
    
    session.sendline("show run")
    session.expect(["#", pexpect.TIMEOUT])
    
    with open("config.txt", "w") as f:
        f.write(session.before)
        f.close()
    print("The running configuration has been saved to config.txt")

#ssh connection with pexpect    
def ssh_connection():
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

def menu():
    
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~ Welcome! ~~~~~~~~~~~~~~~~~~~~~~~")
    print("Please choose a way to remotely connect to a device,")
    print("      and extract the currently running config")
    print("")
    print("1. Telnet")
    print("2. SSH")
    print("3. Quit")
    print("")
    
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
