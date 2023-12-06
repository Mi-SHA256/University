

class Net():
    
    def __init__(self, name, ip, user='cisco', pw='cisco'):
        self.name = name
        self.ip = ip
        self.user = user
        self.password = pw
        self.ow_type = 'unknown'
        

class NetIOS(Net):
    
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco'):
        Net.__init__(self, name, ip, user, pw)
        self.os_type = 'ios'

class NetXR(Net):
        
    def __init__(self, name, ip, user = 'cisco', pw = 'cisco'):
        Net.__init__(self, name, ip, user, pw)
        self.os_type = 'ios-xr'
        
def read_dev_info(devices_file):    
    
    devices_list = []
    
    file = open(devices_file, 'r')
    for line in file:
        device_info = line.strip().split(',')
        
        if device_info[1] == 'ios':
            
            device = NetIOS(device_info[0], device_info[2],
                            device_info[3], device_info[4])
            
        elif device_info [1] == 'ios-xr':
            
            device = NetXR(device_info[0], device_info[2],
                           device_info[3], device_info[4])
            
        else:
            continue
        
        devices_list.append(device)
        
    file.close()
    return devices_list

def print_info(devices_list):
    
    print('')
    print('Name OS-type IP address Username Password')
    print('------ ------- -------------- -------- --------')
    # Go through the list of devices, displaying values in nice format
    for device in devices_list:
        print('{0:8} {1:8} {2:16} {3:8} {4:8}'.format(device.name,
                                                      device.os_type,
                                                      device.ip,
                                                      device.user,
                                                      device.password))
    print('')
    
    
devices = read_dev_info('devices-12.txt')
print_info(devices)

