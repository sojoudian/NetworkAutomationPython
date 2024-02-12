from netmiko import ConnectHandler
cisco_device ={
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,
    'secret': 'cisco',
}
with ConnectHandler(**cisco_device) as netConnection:
    netConnection.enable()
    print(netConnection.send_command('show version'))
