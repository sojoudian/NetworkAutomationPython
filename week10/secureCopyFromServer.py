from pClass import Connector
import time
import os
from datetime import datetime
import sys

try:
    startTime = time.time()
    c = Connector(username="student", password="student", host="192.168.122.1", port=22)
    configFile="sshd_config"
    remotePath="/etc/ssh/"+configFile
    result = c.send_shell_command(f"cat {remotePath}")

    curentTime= datetime.now().strftime('%Y%m%d_%H%M%S')
    localFileName= f"{configFile}_{curentTime}.txt"

    with open(localFileName, "w") as fileName:
        fileName.write(result)
    endTime= time.time()
    print(f"Script took {endTime-startTime} second(s)")
except Exception as e:
    print(e, fileName=sys.stderr)