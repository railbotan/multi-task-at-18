from hashlib import md5
from random import choice
import concurrent.futures
import time

def get_coin(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ',' + h

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for coin in zip(executor.map(get_coin, range(2))):
            print(coin)

if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print(finish - start)