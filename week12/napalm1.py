import napalm

driver = napalm.get_network_driver('ios')

device= driver(hostname='192.168.122.30', username='u1', password='cisco')

device.open()
s
device.close()