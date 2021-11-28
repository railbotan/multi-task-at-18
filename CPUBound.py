import concurrent.futures as cf
from hashlib import md5
from random import choice


def get_coin_and_hash():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("0000"):
            print(s, h)
            break


def main():
    with cf.ProcessPoolExecutor(max_workers=61) as executor:
        [executor.submit(get_coin_and_hash) for _ in range(30)]


if __name__ == '__main__':
    main()
