import threading
import time
import random

# def threadWorker():
#     print("My Thread has entered the 'Running' State")
#
#     time.sleep(10)
#
#     print("My Thread is terminating")
#
# myThread = threading.Thread(target=threadWorker)
#
# myThread.start()
#
# myThread.join()
#
# print("My Thread has entered a 'Dead' State")


def executeThread(i):
    print("Thread {} started0".format(i))
    sleepTime = random.randint(1,10)
    time.sleep(sleepTime)
    print("Thread {} finished executing".format(i))


for i in range(10):
    thread = threading.Thread(target=executeThread, args=(i,))
    thread.start()

    print("Active Threads: ", threading.enumerate())