import telnetlib
import time

# Replace these with actual server address, username, and password
HOST = "192.168.122.20"
PORT = 23
USERNAME = "u1"
PASSWORD = "cisco"

# Connect to the server
tn = telnetlib.Telnet(HOST, PORT)

# Login
tn.read_until("login: ".encode())
tn.write(USERNAME.encode('ascii') + b"\n")
if PASSWORD:
    tn.read_until("Password: ".encode())
    tn.write(PASSWORD.encode('ascii') + b"\n")

# Send a command
tn.write("show version\n".encode())
tn.write('exit\n'.encode())
# Wait for the command to execute and get the response
time.sleep(2)  # Adjust this based on server response time
output = tn.read_very_eager().decode('ascii')

# Print the response
print(output)

# Close the connection
tn.close()
