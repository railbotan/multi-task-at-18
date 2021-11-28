from hashlib import md5
from random import choice

c = 0
while c < 30:
    s = "".join([choice("0123456789") for i in range(50)])
    h = md5(s.encode('utf8')).hexdigest()

    if h.endswith("0000"):
        print(s, h)
        c += 1
