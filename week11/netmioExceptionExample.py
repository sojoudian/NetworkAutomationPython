from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
cisco_device ={
    'device_type': 'cisco_ios',
    'host': '192.168.122.10',
    'username': 'u1',
    'password': '1234', # change the password to simulate the Authentication Exception
    'port': 22,      #Atkclass code: BP25
    'secret': 'cisco',
}
try:
    netConnection=ConnectHandler(**cisco_device)
    netConnection.enable()
    print(netConnection.send_command('show clock'))
    netConnection.disconnect()
except NetmikoTimeoutException:
    print("Connection timed out.")
except NetmikoAuthenticationException:
    print("Authentication failed")