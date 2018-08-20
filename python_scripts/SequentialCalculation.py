import time
import random

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


def main():
    print("Starting number crunching")
    t0 = time.time()

    for i in range(100000):
        rand = random.randint(20000, 10000000)
        print(calculatePrimeFactors(rand))

    t1 = time.time()
    totalTime = t1 - t0

    print("Execution Time = {}".format(totalTime))

if __name__ == '__main__':
    main()