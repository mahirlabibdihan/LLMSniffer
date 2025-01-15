
mod = 1000000007

def mod_exp(b, e, m):
    res = 1
    b %= m
    while e:
        if e&1: res = (res*b) % m
        e >>= 1
        b = (b*b) % m
    return res
    
for _ in range(int(input())):
    n = int(input())
    b = int(bin(n)[2:])
    print (mod_exp(2, 2*b, mod))
    