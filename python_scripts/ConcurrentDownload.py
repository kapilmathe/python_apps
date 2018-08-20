import threading
import urllib.request
import time
import os

def downloadImage(imagepath, filename):
    print("downloading image")
    urllib.request.urlretrieve(imagepath, filename)
    print("Completed download")


def executeThread(i):
    imageName =  "/home/kmathe/codes/python_apps/temp/image-"+str(i)+".jpg"
    downloadImage("http://lorempixel.com/400/200/sports/", imageName)


def main():
    t0 = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,))
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()

    t1 = time.time()
    totalTime = t1 - t0
    print("Total Execution time {}".format(totalTime))

if __name__ == '__main__':
    main()