from pClass import Connector

p = Connector(
            host="192.168.122.1",
            username="student",
            password="student",
            port=22
)

#send a command to the remote host
resultOne = p.send_shell_command("whoami")
print(resultOne)
print("*"*50)