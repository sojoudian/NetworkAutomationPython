import os
import paramiko
import datetime

remoteHost = '192.168.122.1'
remotePort=22
Rusername='student'
Rpassword='student'
remotePath='/home/student'
localPath='file.txt'

sshclient = paramiko.SSHClient()
sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    sshclient.connect(remoteHost, port=remotePort, username=Rusername, password=Rpassword)
    sftp = sshclient.open_sftp()

    curentTime= datetime.datetime.now().strftime('%Y%m%d')

    fileName, fileExtention = os.path.splitext(os.path.basename(localPath))
    newFileName = f"{fileName}_{curentTime}{fileExtention}"

    remoteFilePath = os.path.join(remotePath, newFileName) #/home/student/file_20231108.txt

    sftp.put(localPath, remoteFilePath)
    print(f"File copied to {remoteFilePath} successfully.")
except Exception as e:
    print(f"An error occured: {e}")

finally:
    if sshclient:
        sftp.close()
        sshclient.close()