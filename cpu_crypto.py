from hashlib import md5
from random import choice

coins_count = 4
found_coins = 0

while found_coins != coins_count:
    coin_code = "".join([choice("0123456789") for i in range(50)])
    coin_hash = md5(coin_code.encode('utf8')).hexdigest()

    if coin_hash.endswith("00000"):
        found_coins += 1
        print(f"{found_coins} coins found. Coin code: {coin_code}; Coin hash: {coin_hash};")
