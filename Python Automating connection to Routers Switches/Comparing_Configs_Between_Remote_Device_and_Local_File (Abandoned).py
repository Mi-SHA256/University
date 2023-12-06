import pexpect
from difflib import Differ

ip_address = input("Enter IP address: ")
username = input("Enter Username: ")
password = input("Enter Password: ")

def ssh_config_compare():
    
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

    session.sendline("show startup")
    session.expect(["#", pexpect.TIMEOUT])

    with open("startup_config_ssh.txt", "w") as q:
        q.write(session.before)
        q.close()

    with open("running_config_ssh.txt") as file1, open("startup_config_ssh.txt") as file2:
        differ = Differ()

        for line in differ.compare(file1.readlines(), file2.readlines()):
            with open("difference.txt", "w") as w:
                w.write(line)
                w.close()
    print("Comparison has been saved in difference.txt")
ssh_config_compare()