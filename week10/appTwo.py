import time
import threading

def printNumbers(taskName):
    for i in range(1, 6):
        print(f"{taskName} prints: {i}")
        time.sleep(1) #a second delay

# Creating threads for two tasks ### I will wait till 11:28
theardOne = threading.Thread(target=printNumbers, args=("Task 1",))
threadTwo = threading.Thread(target=printNumbers, args=("Task 2",))
# Start the threads
theardOne.start()
threadTwo.start()
# Joining threads to wait for finishing their computation
theardOne.join()
threadTwo.join()

print("All done!")