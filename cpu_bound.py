import time
import random
from hashlib import md5

coins_count = 5
coin_length = 50
digits = "0123456789"
start = time.time()
coins = 0

print(1)
while coins != coins_count:
    s = "".join(random.choices(digits, k=coin_length))
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("00000"):
        coins += 1
        print(s, h)

all_time = time.time() - start
print(f"Время работы: {all_time:.3f} секунд(ы).")
