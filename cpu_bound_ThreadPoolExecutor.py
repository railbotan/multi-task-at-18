import time
import random
import concurrent.futures
from hashlib import md5

thread_count = 100
coins_count = 5
coin_length = 50
digits = "0123456789"
start = time.time()


def generate_coin():
    while True:
        s = "".join(random.choices(digits, k=coin_length))

        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return s, h


print(thread_count)

with concurrent.futures.ThreadPoolExecutor(thread_count) as executor:
    futures = [executor.submit(generate_coin) for i in range(coins_count)]
    for future in concurrent.futures.as_completed(futures):
        print(*future.result())


all_time = time.time() - start
print(f"Время работы: {all_time:.3f} секунд(ы).")
