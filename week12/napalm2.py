import napalm

driver = napalm.get_network_driver('ios')

device= driver(hostname='192.168.122.20', username='u1', password='cisco', optional_args={"port": 22, "secret": "cisco"})


device.open()
info = device.get_facts()
print("Device Information:")
print(info)
device.close()