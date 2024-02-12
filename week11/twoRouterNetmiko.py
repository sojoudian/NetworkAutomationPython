import threading
from netmiko import ConnectHandler
device_list = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.122.10',
        'username': 'u1',
        'password': 'cisco',
        'port': 22,
        'secret': 'cisco',
    },
    {
        'device_type': 'cisco_ios',
        'host': '192.168.122.20',
        'username': 'u1',
        'password': '1234',
        'port': 22,
        'secret': '1233',
    }
]

def connectAndRun(device):
    try:
        with ConnectHandler(**device) as netConnection:
            netConnection.enable()
            output=netConnection.send_command('show clock')
            print(f"Output from device{device['host']}: \n{output}\n")
    except Exception as e:
        print(f"An error occurred with device {device['host']}: {e}")
threads = []
for device in device_list:
    th = threading.Thread(target=connectAndRun, args=(device,))
    th.start()
    threads.append(th)

# to wait for all threads to complete
for th in threads:
    th.join()

print("All tasks are completed!")
