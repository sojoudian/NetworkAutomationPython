from conn import *
suRoot = "sudo su\n"
command="cat /etc/passwd\n"
shell = ssh_client.invoke_shell()
shell.send(suRoot)
shell.send("student\n")
time.sleep(1)
shell.send(command)
time.sleep(1)
print(shell.recv(80000).decode('utf-8'))