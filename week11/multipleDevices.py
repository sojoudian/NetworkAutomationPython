from netmiko import ConnectHandler
from myDevices import device_list as devices
from datetime import datetime
import threading

def showClock(a_device):
    """Excute show clock command using Netmiko."""
    try:
        remoteConnection=ConnectHandler(**a_device)
        print("#" * 80)
        print(remoteConnection.send_command("show clock"))
        print("#" * 80)
    except Exception as e:
        print(f"An error occurd with device {a_device['host']}: {e}\n")
    finally:
        remoteConnection.disconnect()

def main():
    """
        Use threads and Netmiko to connect to each device. Execute the 'show clock' or any
        Other command you wish to run, tou just need to modify the code
        The amount of time spend for each execution would be record.
    """
    startTime = datetime.now()
    threads= []
    for a_device in devices:
        my_thread = threading.Thread(target=showClock, args=(a_device,))
        my_thread.start()
        threads.append(my_thread)
    for thread in threads:
        thread.join()

    elapsedTime = datetime.now() - startTime
    print("\nElapsed time: "+str(elapsedTime))

if __name__ == "__main__":
    main()