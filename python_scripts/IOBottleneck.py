import urllib.request
import time

t0 = time.time()
req = urllib.request.urlopen('http://www.google.com')
pageHTML = req.read()
t1 = time.time()
print("Total time to fetch page: {} Seconds".format(t1-t0))