
import pexpect
import difflib

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
    
    session.sendline("show user")
    session.expect(["#", pexpect.TIMEOUT])
    
    print(session.before)




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
    
    session.sendline("show user")
    session.expect(["#", pexpect.TIMEOUT])
    
    print(session.before)

def ssh_config():
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


def menu():
    
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~ Welcome! ~~~~~~~~~~~~~~~~~~~~~~~")
    print("               Please choose an option")
    print("")
    print("1. Telnet")
    print("2. SSH")
    print("3. Save config file via secure connection")
    print("4. Compare running and startup config")
    print("5. Compare running config to backed-up file")
    print("")
    print("6. Quit")
    
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
        print("Goodbye!")  
    else:
        print("Choice is not valid. ")
    
menu()
