from decimal import *
for _ in range(int(input())):
    n,k = map(int,input().split())
    if n >= 1000 :q1 = str(int(pow(10, (Decimal(n) *(Decimal(n).log10()))%1 + k -1)))
    else: q1 = str(n**n)[:k]               
    print(q1 + " " + str(pow(n, n, 10 ** k)).zfill(k))