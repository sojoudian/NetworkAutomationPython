import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.122.100', username='u1', password='cisco', port=22)
time.sleep(1)
sConn = ssh_client.get_transport().is_active()
print("Successful connection", sConn)