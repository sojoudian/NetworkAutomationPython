from netmiko import ConnectHandler

cisco_device ={
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
}
netConnect = ConnectHandler(**cisco_device)
#enable mode
netConnect.enable()
configCommand = ['int loopback 0', 'ip address 2.2.2.2 255.255.255.0']
#output = netConnect.send_config_set(configCommand)
#print(output)
print(netConnect.send_config_set(configCommand))
netConnect.disconnect()