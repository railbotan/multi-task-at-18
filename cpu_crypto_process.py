import concurrent.futures as futures
from hashlib import md5
from random import choice


def find_coin(n):
    while True:
        coin_code = "".join([choice("0123456789") for i in range(50)])
        coin_hash = md5(coin_code.encode('utf8')).hexdigest()

        if coin_hash.endswith("00000"):
            return f"Coin code: {coin_code}; Coin hash: {coin_hash};"


def main():
    coins_count = 4
    with futures.ProcessPoolExecutor(max_workers=100) as executor:
        for coin in zip(executor.map(find_coin, range(coins_count))):
            print(coin)


if __name__ == '__main__':
    main()
