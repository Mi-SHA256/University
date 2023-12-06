import pexpect

class NetDev():
    
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco123!'):
        self.name = name 
        self.ip_address = ip
        self.username = user
        self.password = pw
        self.interfaces = ''
        
    def connect(self):
        self.session = None
        
    def get_int(self):
        self.interfaces = '--- Base Device, unknown get interfaces ---'
        
class NetIOS(NetDev):
    
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco123!'):
        NetDev.__init__(self, name, ip, user, pw)
    
    def connect(self):
        
        print('--- connecting IOS: telnet ' + self.ip_address)
        
        self.session = pexpect.spawn('telnet ' + self.ip_address,
                                     encoding = 'utf-8', timeout = 20)
        
        self.session.expect(['Username:', pexpect.TIMEOUT, pexpect.EOF])
        self.session.sendline(self.username)
        
        self.session.expect(['Password:', pexpect.TIMEOUT, pexpect.EOF])
        self.session.sendline(self.password)
        
        self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
        self.session.sendline('terminal length 0')
        
        self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
        
    def interfaces(self):
        
        self.sesion.sendline('show int sum')
        self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
        
        self.interfaces = self.session.before
        
class NetXR(NetDev):
    
    def __init__(self, name, ip, user = 'cisco', pw= 'cisco123!'):
        NetDev.__init__(self, name, ip, user, pw)
        
    def connect(self):
        
        print('--- connection XR: ssh' + self.username + '@' + self.ip_address)
        
        
    def terminal(self):
        
        self.session.sendline('terminal length 0')
        self.session.expect(['>', pexpect.TIMEOUT, pexpect.EOF])
        
    def interfaces_(self):
        
        self.interfaces = '--- XR Device interface info ---'
        
def read_info(devices_file):
    
    devices_list = []
    
    file = open(devices_file, 'r')
    for line in file:
        device_info = line.strip().split(',')
        
        if device_info[1] == 'ios':
            
            device = NetIOS(device_info[0], device_info[2],
                            device_info[3], device_info[4])
            
        elif device_info[1] == 'ios-xr':
            
            device = NetXR(device_info[0], device_info[2],
                           device_info[3], device_info[4])
        else:
            device = NetDev(device_info[0], device_info[2],
                           device_info[3], device_info[4])
       
        devices_list.append(device)
   
    file.close()
    return devices_list

def print_info(device):
    
    print("--------------------------------------------------------------------")
    print(" Device Name: ", device.name)
    print(" Device IP  : ", device.ip_address)
    print(" Device User: ", device.username)
    print(" Device Pass: ", device.password)
    
    print("")
    print("                  Showing Interfaces")
    print("")
    
    print(device.interfaces)
    print("--------------------------------------------------------------------")

devices_list = read_info('devices-13.txt')    
for device in devices_list:
    
    print('========= Device ==============================================================')
    
    session = device.connect()
    device.interfaces_()
    print_info(device)