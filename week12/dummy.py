from telnetlib import Telnet
import time

t = Telnet(host='192.168.122.20', port=23)

t.read_until("Username:".encode())
# t.write("maziar\n".encode())
t.write(b'u1\n')

#read text "password"
t.read_until("Password:".encode())
t.write(b'cisco\n')
time.sleep(2)
t.write(b'terminal length 0\n')
time.sleep(2)
#then input the cisco password

t.write('show version\n'.encode())
time.sleep(2)
t.write('exit\n'.encode())
print(t.read_all().decode())