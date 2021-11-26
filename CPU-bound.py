from hashlib import md5
from random import choice
import concurrent.futures
from time import time


def is_prime(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ',' + h


def main():
    time1 = time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        for answer in zip(executor.map(is_prime, range(3))):
            print(answer)
    time2 = time()
    print(time2 - time1)


if __name__ == '__main__':
    main()
