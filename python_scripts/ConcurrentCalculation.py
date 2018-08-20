import time
import random
from multiprocessing import Process

def calculatePrimeFactors(n):
    primFac = []
    d = 2
    while d*d <= n:
        while (n% d) == 0:
            primFac.append(d)
            n //=d
        d += 1
    if n > 1:
        primFac.append(n)
    return primFac

def execProc():
    for i in range(10000):
        rand = random.randint(20000, 100000000)
        print(calculatePrimeFactors(rand))


def main():
    print("Starting number crunching")
    t0 = time.time()

    procs = []

    for i in range(10):
        proc = Process(target=execProc, args=())
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    t1 = time.time()
    totalTime = t1 - t0

    print("Execution time: {}".format(totalTime))

if __name__ == '__main__':
    main()