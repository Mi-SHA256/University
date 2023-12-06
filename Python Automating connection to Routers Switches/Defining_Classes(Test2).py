
class NetDev():
    
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco'):
        self.name = name 
        self.ip_address = ip
        self.username = user
        self.password = pw
        
    def get_type(self):
        return 'base'
    
class NetIOS():
    
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco'):
        NetDev.__init__(self, name, ip, user, pw)
        
    def get_type(self):
        return 'IOS'
    
class NetXR():
    
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco'):
        NetDev.__init__(self, name, ip, user, pw)
        
    def get_type(self):
        return 'IOS-XR'
    
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

def print_info(devices_list):
    
    print('')
    print('Name   OS-type IP address     Username Password')
    print('------ ------- -------------- -------- --------')
    for device in devices_list:
        print('{0:8} {1:8} {2:16} {3:8} {4:8}'.format(device.name,
                                                      device.os_type,
                                                      device.ip_address,
                                                      device.username,
                                                      device.password))
    print('')
    
devices = read_info('devices-12.txt')
print_info(devices)