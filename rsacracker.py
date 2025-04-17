from Crypto.PublicKey import RSA
from pwn import *
from sage.all import *

e = key.e
n = key.n
p, q = factor(n)
p = int(p[0])
q = int(q[0])

log.info(f"e: {e}")
log.info(f"n: {n}")
log.info(f"p: {p}")
log.info(f"q: {q}")

m = n-(p+q-1)
log.info(f"m: {m}")

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
def modinv(a, m):
    g, x, y =egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
d = modinv(e, m)
log.info(f"d: {d}")

privateKey = RSA.construct((n, e, d, p, q))
print(f"\n\n[+] Listando la clave privada:\n\n")
print(privateKey.exportKey().decode())
