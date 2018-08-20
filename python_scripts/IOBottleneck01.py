import urllib.request
import time
from bs4 import BeautifulSoup

t0 = time.time()
req = urllib.request.urlopen('http://www.examples.com')
t1 = time.time()
print("Total time to fetch page: {} Seconds".format(t1-t0))
soup = BeautifulSoup(req.read(), "html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))


t2 = time.time()
print("Total Execution time2 : {} Seconds".format(t2-t1))