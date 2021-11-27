import concurrent.futures
import time
from hashlib import md5
from random import choice

def get_coins(n):
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s + ',' + h


#def is_prime(n):
#    if n < 2:
#        return False
#    if n == 2:
#        return True
#    if n % 2 == 0:
#        return False
#
#    sqrt_n = int(math.floor(math.sqrt(n)))
#    for i in range(3, sqrt_n + 1, 2):
#        if n % i == 0:
#            return False
#    return True

def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=100) as executor:
        for coin in zip(executor.map(get_coins, range(3))):
            print(coin)

if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print(finish - start)



