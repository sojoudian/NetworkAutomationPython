import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.122.1', username='student', password='student', port=22)
print("Successful connection", ssh_client.get_transport().is_active())