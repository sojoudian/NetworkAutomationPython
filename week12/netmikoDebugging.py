import time
import logging
from netmiko import ConnectHandler

logging.basicConfig(filename='Nov-22-03.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

net_connect = ConnectHandler(host='192.168.122.10', username="u1", password="cisco", device_type="cisco_ios")

print(net_connect.find_prompt())
print("*" * 100)
net_connect.write_channel("show version\n")
time.sleep(2)
outPut=net_connect.read_channel()

net_connect.disconnect()