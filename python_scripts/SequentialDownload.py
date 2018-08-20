import threading
import urllib.request
import time
import os

def downloadImage(imagepath, filename):
    print("downloading image")
    urllib.request.urlretrieve(imagepath, filename)
    print("Completed image")


def main():
    t0 = time.time()
    for i in range(10):
        imageName = "/home/kmathe/codes/python_apps/temp/image-"+str(i)+".jpg"
        downloadImage("http://lorempixel.com/400/200/sports/", imageName)

    t1 =time.time()
    totalTime = t1-t0
    print("Total Execution time {}".format(totalTime))


if __name__ == '__main__':
    main()