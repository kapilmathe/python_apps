import threading
import time

def standardThread():
    print("Starting my Standard Thread")
    time.sleep(20)
    print("Ending my Standard Thread")

def daemonThread():
    while True:
        print("Sending Out HeartBeat Signal")
        time.sleep(2)

if __name__ == '__main__':
    standardthread = threading.Thread(target=standardThread)
    daemonthread = threading.Thread(target=daemonThread)
    daemonthread.setDaemon(True)
    daemonthread.start()

    standardthread.start()