from conn import *


stdin, stdout, stderr = ssh_client.exec_command("ls\n")
time.sleep(1)
output = stdout.read().decode('utf-8')
print(output)

listView = output.split('\n')
print(listView)




# shell = ssh_client.invoke_shell()
# shell.send("ls\n")
# time.sleep(1)
# respone = shell.recv(1000) #receive 1000 bytes
# result = respone.decode('utf-8')
#print(result)

#print("+++++++++++++++++++++++++++++++++++++")