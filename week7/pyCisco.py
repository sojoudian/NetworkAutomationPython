from pClass import Connector

p = Connector(
            host="192.168.122.100",
            username="u1",
            password="cisco",
            port=22
)

#send a command to the remote host
resultOne = p.send_shell_command("show run")
print(resultOne)
print("*"*50)