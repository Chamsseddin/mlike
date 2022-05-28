import mlike
from time import sleep

n = 555976553 #779759253

for i in range(n, n + 100):
    c = mlike.Client(n).set_credit()
    print(c)
    if (c['status'] == 200):
        sleep(10)
        continue
    else:
        sleep(30)
        mlike.Client(n).set_credit()
