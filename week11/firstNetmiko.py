from netmiko import ConnectHandler
cisco_device ={
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
}
netConnect= ConnectHandler(**cisco_device)
#Enter the enable mode

#print(f'{}')
netConnect.enable()
result=netConnect.send_command('show ip int brief')
print(result)
netConnect.disconnect()